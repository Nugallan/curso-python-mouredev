from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # importamos 2 clases para manejar autenticación
from jose import jwt, JWTError # importamos librería de encriptación
from passlib.context import CryptContext # importamos la librería passlib para la encriptación
from datetime import datetime, timedelta
# JWT: "JSON Web Token"

# Inicia el servidor: uvicorn jwt_auth_users:app --reload

# Algoritmo de encriptación
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 # indicamos duración de 1 minuto
SECRET = "48a5b86f00309eb442ab36987023b3804f285259d5d9b961c47293499149bd61" # con el comando 'openssl rand --hex 32' generamos una clave aleatoria de longitud hexadecimal de 32

router = APIRouter()

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto") # algoritmo de encriptación y 'deprecated' por si afecta a versiones de 'passlib'

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
    "password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6" # Algoritmo de hash obtenido al introducir como contraseña '123456' en https://bcrypt-generator.com
  },
  "mouredev2": {
    "username": "mouredev2",
    "full_name": "Brais Moure 2",
    "email": "braismoure2@mouredev.com",
    "disabled": True,
    "password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU4S" # Algoritmo de hash obtenido al introducir como contraseña '654321' en https://bcrypt-generator.com
  },
}

# funciones auxiliares
def search_user_db(username: str): # Buena costumbre poner tipo de datos
  if username in users_db:
    return UserDB(**users_db[username])

def search_user(username: str):
  if username in users_db:
    return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):

  exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED, # con status. nos ayuda a escoger un tipo de error más adecuado
      detail="Credenciales de autenticación inválidas",
      headers={"WWW-Authenticate": "Bearer"}
    )

  try:
    username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub") # Decodificamos pasando el token, SECRET y algoritmo
    if username is None: # Por si por ejemplo 'sub' viene vacío
      raise exception

  except JWTError:
    raise exception

  return search_user(username)


# Criterio de dependencia
async def current_user(user: User = Depends(auth_user)): # tomamos la función 'auth_user

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

  if not crypt.verify(form.password, user.password): # le pasamos la contraseña que viene por el formulario y la contraseña encriptada de nuestra BD
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

  # Generamos un 'access token' con un json y el cálculo del tiempo de expiración
  access_token = {"sub":user.username,
                  "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)} # exp cuando expira

  # JSON que va a devolver el "access_token" que creamos antes, la variable SECRET y el algoritmo de la variable ALGORITHM que hicimos antes
  return {
      "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
      "token_type": "bearer"
  }


@router.get("/users/me")
async def me(user: User = Depends(current_user)): # Criterios de dependencia llamando a la función 'current_user'
  return user
