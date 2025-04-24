from fastapi import APIRouter # Aquí ya no importamos 'FastAPI' como hacíamos antes

# Y aquí ya no definimos hacíamos como la app principal (app = FastAPI())
router = APIRouter(
                   prefix="/products", # Con el prefijo 'prefix="/products"' no tendremos que indicar la ruta "/products" en las próximas funciones
                   tags=["products"], # Crea una agrupación propia de'products' para el doc de 'http://127.0.0.1:8000/docs'
                   responses={404: {"message": "No encontrado"}} # Con 'responses' añadimos un código de error y un mensaje
                  )

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

# Aquí no sería '@app' como antes, sino @router
@router.get("/") # no hace falta poner '/products' ya que lo indicamos como prefijo antes
async def products():
  return products_list

@router.get("/{id}")
async def products(id: int):
  return products_list[id]
