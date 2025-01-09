import redis
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)


baseDatosRedis.set("libro_1","Quijote")
baseDatosRedis.set("libro_2","Hamlet")
baseDatosRedis.set("libro_3","Otelo")
baseDatosRedis.set("comic_1","Mortadelo y Filemón")
baseDatosRedis.set("comic_2","Superman")

print("Los Libros:")
for clave in baseDatosRedis.scan_iter('libro*'):
   print(clave)
  
print("Los Comics:")   
for clave in baseDatosRedis.scan_iter('comic*'):
   print(clave)

def main():
    # Función 1: Crear registros clave-valor
    print("\n1. Crear registros clave-valor")
    client.set("inem:nombre", "INEM 2.0")
    client.set("inem:sector", "Empleo y Formación")
    print("Registros creados: 'inem:nombre' y 'inem:sector'.")

    # Función 2: Obtener y mostrar el número de claves registradas
    print("\n2. Obtener y mostrar el número de claves registradas")
    keys = client.keys()
    print(f"Número de claves registradas: {len(keys)}")

    # Función 3: Obtener y mostrar un registro en base a una clave
    print("\n3. Obtener y mostrar un registro en base a una clave")
    value = client.get("inem:nombre")
    print(f"Valor de 'inem:nombre': {value}")

    # Función 4: Actualizar el valor de una clave y mostrar el nuevo valor
    print("\n4. Actualizar el valor de una clave y mostrar el nuevo valor")
    client.set("inem:nombre", "INEM 2.0 Actualizado")
    updated_value = client.get("inem:nombre")
    print(f"Nuevo valor de 'inem:nombre': {updated_value}")

    # Función 5: Eliminar una clave-valor y mostrar la clave y el valor eliminado
    print("\n5. Eliminar una clave-valor y mostrar la clave y el valor eliminado")
    deleted_value = client.get("inem:sector")
    client.delete("inem:sector")
    print(f"Clave eliminada: 'inem:sector', Valor eliminado: {deleted_value}")

    # Función 6: Obtener y mostrar todas las claves guardadas
    print("\n6. Obtener y mostrar todas las claves guardadas")
    keys = client.keys()
    print(f"Claves guardadas: {keys}")
    
    # Función 7: Obtener y mostrar todos los valores guardados
    print("\n7. Obtener y mostrar todos los valores guardados")
    values = [client.get(key) for key in keys]
    print(f"Valores guardados: {values}")