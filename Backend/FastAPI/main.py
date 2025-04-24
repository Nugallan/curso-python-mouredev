from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db # Importamos products.py y users.py, archivos de autenticación del paquete y users_db 'routers'
from fastapi.staticfiles import StaticFiles # para carga de imágenes, documentos, etc estáticos
# uvicorn main:app --reload # <- escribir en terminal. 'uvicorn' es un servidor que ofrece FastAPI; 'main' es el archivo que queremos arrancar; 'app' es la instancia de FastAPI; '--reload' argumento que recarga el contexto del servidor cada vez que cambiamos el fichero 'main'

# Contexto inicial de FastAPI
app = FastAPI()

# Routers (Incluimos en la app principal el router de productos.py, users.py y archivos de autenticación)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

# Recursos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static") # 'mount' monta recursos estáticos

@app.get("/") # con '@app' accedemos al contexto de FastAPI
async def root(): # Siempre que llamamos a un servidor la operación tiene que ser asíncrona
  return "¡Hola FastAPI!"

@app.get("/url") # Aplicando en el path /url. Para verlo en el navegador: http://127.0.0.1:8000/url
async def url():
  return {"url_curso":"https://mouredev.com/python"}

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
