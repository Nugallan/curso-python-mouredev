#from ast import Try
from fastapi import APIRouter, HTTPException # HTTPException para lanzar excepciones de requests
from pydantic import BaseModel  # BaseModel nos permite crear entidades

### API referida a Users ###

# Y aquí ya no definimos hacíamos como la app principal (app = FastAPI())
router = APIRouter(
                   prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}}
  )

# Entidad user
class User(BaseModel):  # nos da la capacidad de crear una entidad
    id: int
    name: str
    surname: str
    url: str
    age: int

# Imaginamos que es lo que tendríamos en una BBDD
users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Borja", surname="Dev", url="https://borja.dev", age=39),
    User(id=3, name="Haakon", surname="Dahlgberg", url="https://haakon.com", age=45),
]

@router.get("/usersjson")
async def usersjson(): # Creamos un JSON a mano
    return [
        {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
        {"name": "Borja", "surname": "Dev", "url": "https://borja.dev", "age": 39},
        {"name": "Haakon", "surname": "Dahlgberg", "url": "https://haakon.com", "age": 46,},
    ]

# GET
@router.get("/") # A partir de ahora no hará falta añadir "/users" gracias al prefix
async def users():
    return users_list

# Path
@router.get("/{id}")
async def user(id: int): # indicamos que el 'id' sea un entero
  return search_user(id)

# Query
@router.get("/")
#async def user(id: int, name: str): # Ejemplo de hacer una búsqueda por los dos -> P.E: http://127.0.0.1:8000/user/?id=!&name=Brais
async def user(id: int):
  return search_user(id)


# POST
# Añadir un nuevo usuario
@router.post("/", response_model=User, status_code=201) # 'response_model=User', 'status_code=201' indicamos que por defecto devuelva '201 Created'
async def user(user: User): # Antes creamos nuestro obj y FastAPI se encarga de transformar JSON en un usuario
  if type(search_user(user.id)) == User:
    # 'raise' sirve para lanzar excepciones manualmente. Interrumpe el flujo del programa y genera un error que debe ser manejado
    raise HTTPException(status_code=409, detail="El usuario ya existe") # lanza un "status=409 Conflict" y añado un "detail": "El usuario ya existe"
  else:
    users_list.append(user)
    return {"message":"Usuario creado", "user": user}


# PUT (Actualiza)
@router.put("/")
async def user(user: User): # Le pasamos el usuario a actualizar

  found = False

  for index, saved_user in enumerate(users_list): # Para saber la posición del usuario usamos 'enumerate'
    if saved_user.id == user.id:
      users_list[index] = user
      found = True

  if not found:
    return {"error":"No se ha actualizado el usuario"}
  else:
    return user


# DELETE
@router.delete("/{id}")
async def user(id: int):

  found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]
      found = True

  if not found:
    return {"error":"No se ha eliminado el usuario"}
  else:
    return {"message":"Usuario eliminado correctamente"}

# Función para buscar un usuario
def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list) # 'filter' es una función de orden superior
  try:
    return list(users)[0]
  except:
    return {"error":"No se ha encontrado al usuario"}
