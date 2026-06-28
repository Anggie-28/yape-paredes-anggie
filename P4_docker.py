"""
Parte D - MongoDB local con Docker
Estudiante: Anggie Paredes Becerra
Codigo: 2221841736

Comandos previos en PowerShell:
docker pull mongo:7.0
docker run -d --name yape-mongo-local -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=yape2026 mongo:7.0
docker ps
"""

from pymongo import MongoClient


client_docker = MongoClient(
    "mongodb://admin:yape2026@localhost:27017/",
    authSource="admin",
)

db_local = client_docker["yape_local"]
col_local = db_local["comerciantes_test"]

# Limpiar el registro de prueba para que el output sea claro si se ejecuta varias veces.
col_local.delete_many({"nombre_comercio": "Bodega Test Docker"})

col_local.insert_one(
    {
        "nombre_comercio": "Bodega Test Docker",
        "tipo": "bodega",
        "distrito": "Lima",
        "monto_mensual_soles": 1500.00,
        "yape_activo": True,
        "entorno": "docker_local",
    }
)

doc = col_local.find_one({"nombre_comercio": "Bodega Test Docker"})
print("Documento guardado en MongoDB Docker:")
print(f"   Nombre:   {doc['nombre_comercio']}")
print(f"   Entorno:  {doc['entorno']}")
print(f"   ID:       {doc['_id']}")

print(f"\nTotal documentos en Docker: {col_local.count_documents({})}")
