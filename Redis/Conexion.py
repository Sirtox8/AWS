import redis
import json
import os

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

def connect_to_redis():
    return redis.StrictRedis(host='localhost', port=6379, decode_responses=True)


# 1. Crear registros clave-valor
def create_records(client):
    client.set("inem:nombre", "INEM 2.0")
    client.set("inem:sector", "Empleo y Formación")
    client.set("empleado:1", json.dumps({"nombre": "Juan", "edad": 30}))
    client.set("empleado:2", json.dumps({"nombre": "Ana", "edad": 25}))
    print("Registros creados.")

# 2. Obtener y mostrar el número de claves registradas
def count_keys(client):
    print("Número de claves registradas:", len(client.keys("*")))

# 3. Obtener y mostrar un registro en base a una clave
def get_record(client, key):
    value = client.get(key)
    print(f"Valor de '{key}':", value)

# 4. Actualizar el valor de una clave y mostrar el nuevo valor
def update_record(client, key, new_value):
    client.set(key, new_value)
    print(f"Nuevo valor de '{key}':", client.get(key))

# 5. Eliminar una clave-valor y mostrar la clave y el valor eliminado
def delete_record(client, key):
    value = client.get(key)
    client.delete(key)
    print(f"Clave eliminada: '{key}', Valor eliminado: {value}")

# 6. Obtener y mostrar todas las claves guardadas
def get_all_keys(client):
    keys = client.keys("*")
    print("Claves guardadas:", keys)

# 7. Obtener y mostrar todos los valores guardados
def get_all_values(client):
    keys = client.keys("*")
    values = [client.get(key) for key in keys]
    print("Valores guardados:", values)

# 8. Obtener y mostrar varios registros con un patrón usando '*'
def get_records_with_pattern_star(client, pattern):
    keys = client.keys(pattern)
    records = {key: client.get(key) for key in keys}
    print(f"Registros con patrón '{pattern}':", records)

# 9. Obtener registros con patrón usando '[]'
def get_records_with_pattern_brackets(client, pattern):
    keys = client.keys(pattern)
    records = {key: client.get(key) for key in keys}
    print(f"Registros con patrón '{pattern}':", records)

# 10. Obtener registros con patrón usando '?'
def get_records_with_pattern_question(client, pattern):
    keys = client.keys(pattern)
    records = {key: client.get(key) for key in keys}
    print(f"Registros con patrón '{pattern}':", records)

# 11. Filtrar registros por un valor específico
def filter_records_by_value(client, attribute, value):
    keys = client.keys("*")
    matches = []
    for key in keys:
        try:
            data = json.loads(client.get(key))
            if data.get(attribute) == value:
                matches.append({key: data})
        except (TypeError, json.JSONDecodeError):
            continue
    print(f"Registros con {attribute} = {value}:", matches)

# 12. Actualizar registros con un filtro
def update_records_by_filter(client, attribute, increment):
    keys = client.keys("*")
    for key in keys:
        try:
            data = json.loads(client.get(key))
            if attribute in data:
                data[attribute] += increment
                client.set(key, json.dumps(data))
        except (TypeError, json.JSONDecodeError):
            continue
    print(f"Registros con atributo '{attribute}' actualizados.")

# 13. Eliminar registros con un filtro
def delete_records_by_filter(client, attribute):
    keys = client.keys("*")
    for key in keys:
        try:
            data = json.loads(client.get(key))
            if attribute in data:
                client.delete(key)
        except (TypeError, json.JSONDecodeError):
            continue
    print(f"Registros con atributo '{attribute}' eliminados.")

# 14. Crear una estructura JSON de array
def create_json_array(client, key, data):
    client.set(key, json.dumps(data))
    print(f"Estructura JSON guardada en {key}.")

# 15. Filtro por cada atributo de JSON
def filter_json_by_attribute(client, key, attribute, value):
    data = json.loads(client.get(key))
    filtered = [item for item in data if item.get(attribute) == value]
    print(f"Elementos con {attribute} = {value}:", filtered)

# 16. Crear una lista en Redis
def create_list(client, key, values):
    client.delete(key)
    for value in values:
        client.rpush(key, value)
    print(f"Lista '{key}' creada.")

# 17. Obtener elementos de una lista con filtro
def get_list_with_filter(client, key, value):
    elements = client.lrange(key, 0, -1)
    filtered = [elem for elem in elements if value in elem]
    print(f"Elementos filtrados en la lista '{key}':", filtered)

# 18. Usar otros tipos de datos: Set y Hash
def create_set(client, key, values):
    client.sadd(key, *values)
    print(f"Set '{key}' creado con valores: {values}")

def get_set(client, key):
    values = client.smembers(key)
    print(f"Valores del set '{key}':", values)

def create_hash(client, key, data):
    client.hset(key, mapping=data)
    print(f"Hash '{key}' creado.")

def get_hash(client, key):
    data = client.hgetall(key)
    print(f"Datos del hash '{key}':", data)

def main():
    try:
        client = connect_to_redis()
    except ModuleNotFoundError as e:
        print("Error al conectar con Redis. Asegúrese de que está instalado y ejecutándose.")
        return

    print("1. Crear registros clave-valor")
    create_records(client)

    print("\n2. Obtener y mostrar el número de claves registradas")
    count_keys(client)

    print("\n3. Obtener y mostrar un registro en base a una clave")
    get_record(client, "inem:nombre")

    print("\n4. Actualizar el valor de una clave y mostrar el nuevo valor")
    update_record(client, "inem:nombre", "INEM 2.0 Actualizado")

    print("\n5. Eliminar una clave-valor y mostrar la clave y el valor eliminado")
    delete_record(client, "inem:sector")

    print("\n6. Obtener y mostrar todas las claves guardadas")
    get_all_keys(client)

    print("\n7. Obtener y mostrar todos los valores guardados")
    get_all_values(client)

    print("\n8. Obtener y mostrar varios registros con un patrón usando '*'")
    get_records_with_pattern_star(client, "empleado:*")

    print("\n9. Obtener registros con patrón usando '[]'")
    get_records_with_pattern_brackets(client, "empleado:[12]")

    print("\n10. Obtener registros con patrón usando '?'")
    get_records_with_pattern_question(client, "empleado:?")

    print("\n11. Filtrar registros por un valor específico")
    filter_records_by_value(client, "edad", 30)

    print("\n12. Actualizar registros con un filtro")
    update_records_by_filter(client, "edad", 1)

    print("\n13. Eliminar registros con un filtro")
    delete_records_by_filter(client, "edad")

    print("\n14. Crear una estructura JSON de array")
    create_json_array(client, "usuarios_array", [
        {"nombre": "Juan", "edad": 30},
        {"nombre": "Ana", "edad": 25}
    ])

    print("\n15. Filtro por cada atributo de JSON")
    filter_json_by_attribute(client, "usuarios_array", "edad", 25)

    print("\n16. Crear una lista en Redis")
    create_list(client, "mi_lista", ["item1", "item2", "item3"])

    print("\n17. Obtener elementos de una lista con filtro")
    get_list_with_filter(client, "mi_lista", "item2")

    print("\n18. Usar otros tipos de datos: Set y Hash")
    create_set(client, "mi_set", {"valor1", "valor2", "valor3"})
    get_set(client, "mi_set")

    create_hash(client, "mi_hash", {"campo1": "valor1", "campo2": "valor2"})
    get_hash(client, "mi_hash")

if __name__ == "__main__":
    main()
