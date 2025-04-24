# Encargado de gestionar la conexión a la BD de mongoDB
from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local # Creamos el objeto de la BD de mongoDB y añadimos 'local' para evitar poner 'local' en los archivos

# Simulamos una BD de mongoDB en remoto
#Base de datos remota. Enlace generado por la web MongoDB Atlas para usuario test
db_client = MongoClient("mongodb+srv://test:test@cluster0.evfdsyi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test