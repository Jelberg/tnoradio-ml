import psycopg2
import json

# Leer las credenciales de un archivo JSON
def bdConection():
    with open("credentials.json") as archivo_credenciales:
        credenciales = json.load(archivo_credenciales)
    # Como la conexión devuelve un diccionario podemos convertirlo fácilmente

    try:
        conexion = psycopg2.connect(**credenciales)
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)