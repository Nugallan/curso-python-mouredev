from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # importamos 2 clases para manejar autenticación

# Inicia el servidor: uvicorn basic_auth_users:app --reload

router = APIRouter()

# Criterio de autenticación
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Modelos
class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool

class UserDB(User):
  password: str


# Base de datos simulada
users_db = {
  "mouredev": {
    "username": "mouredev",
    "full_name": "Brais Moure",
    "email": "braismoure@mouredev.com",
    "disabled": False,
    "password": "123456" # En un caso real se aplicaría un hash
  },
  "mouredev2": {
    "username": "mouredev2",
    "full_name": "Brais Moure 2",
    "email": "braismoure2@mouredev.com",
    "disabled": True,
    "password": "654321" # En un caso real se aplicaría un hash
  },
}


# Funciones auxiliares
def search_user_db(username: str): # Buena costumbre poner tipo de datos
  if username in users_db:
    return UserDB(**users_db[username]) # Los 2 asteriscos (**) indicamos que pueden ir varios parámetros

def search_user(username: str):
  if username in users_db:
    return User(**users_db[username])


# Criterio de dependencia
async def current_user(token: str = Depends(oauth2)): # token de tipo string buscándolo en el sistema de autenticación (oauth2)
  user = search_user(token) # Buscamos en la BD pasándole el token a la función 'search_user'
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED, # con status. nos ayuda a escoger un tipo de error más adecuado
      detail="Credenciales de autenticación inválidas",
      headers={"WWW-Authenticate": "Bearer"}
      )
  if user.disabled:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Usuario inactivo",
    )

  return user


# Login
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # de tipo form. Indicamos que va a venir de 'Depends' (va a recibir datos pero no "depende" de nadie)
  user_db = users_db.get(form.username) # Buscamos en la BD por get si está el usuario
  if not user_db:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

  user = search_user_db(form.username)
  if not form.password == user.password:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

  # JSON que va a devolver "acces_token" y el tipo ("token_type") bearer (bearer es un estándar)
  return {"access_token": user.username, "token_type": "bearer"} # consideramos que el token de acceso es el nombre del usuario


@router.get("/users/me")
async def me(user: User = Depends(current_user)): # Criterios de dependencia llamando a la función 'current_user'
  return user

