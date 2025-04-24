#from ast import Try
from fastapi import APIRouter, HTTPException, status
from db.models.user import User # Importamos el modelo de usuario
from db.schemas.user import user_schema, users_schema # Importamos user_schema
from db.client import db_client # importamos nuestro cliente
from bson import ObjectId

router = APIRouter(
                   prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
        )


@router.get("/", response_model=list[User]) # response_model=list[User) # Indicamos que la respuesta es una lista de User
async def users():
    return users_schema(db_client.users.find()) # db_client.users.find() # 'find' devuelve todos

@router.get("/{id}")
async def user(id: str): # indicamos que el 'id' sea un entero
  return search_user("_id", ObjectId(id))

@router.get("/")
async def user(id: str):
  return search_user("_id", ObjectId(id))


# POST
# Añadir un nuevo usuario
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
  if type(search_user("email", user.email)) == User:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe") # lanza un "status=409 Conflict" y añado un "detail": "El usuario ya existe"
  
  user_dict = dict(user) # transformamos el usuario en un diccionario ya que básicamente JSON es un diccionario
  del user_dict["id"] # Elimina el campo "id" (si existe)
  
  # Nos conectamos a la BD llamada ' de MongoDB, al esquema 'users' y usamos 'insert_one' para insertar el usuario y el 'id' con el que se ha insertado
  inserted_id = db_client.users.insert_one(user_dict).inserted_id

  # Accedemos a la BD y al esquema 'users' y usamos 'find_one' para buscar el usuario con el 'id' que acabamos de insertar
  new_user = user_schema(db_client.users.find_one({"_id": inserted_id}))
  
  return User(**new_user) # creamos un usuario pasándole todos los campos de 'new_user' con los **

# PUT (Actualiza)
@router.put("/", response_model=User)
async def user(user: User): # Le pasamos el usuario a actualizar

  user_dict = dict(user) # transformamos el usuario en un diccionario ya que básicamente JSON es un diccionario
  del user_dict["id"] # Elimina el campo "id" (si existe)
  
  try:
    db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict) # Actualizamos el usuario por id
  except:
    return {"error":"No se ha actualizado el usuario"}

  return search_user("_id", ObjectId(user.id))

# DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

  found = db_client.users.find_one_and_delete({"_id": ObjectId(id)}) # criterio para eliminarlo por id

  if not found:
    return {"error":"No se ha eliminado el usuario"}


# Función para buscar un usuario
def search_user(field: str, key): # field es el campo y key es el valor del campo
  try:
    user = db_client.users.find_one({field: key})
    return User(**user_schema(user)) # Importante asteriscos antes del diccionario
  except:
    return {"error":"No se ha encontrado al usuario"}