###Python package manager ###

# pip https://pypi.org

# Comandos:
# pip --version (Comprobar si está instalado)
# python get-pip.py (para instalar pip en Windows)

# numpy: biblioteca para la computación científica en Python:

import numpy # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])

print(type(numpy_array))

print(numpy_array * 2)

# pandas: biblioteca especializada en manipulación y análisis de datos estructurados construida sobre NumPy
import pandas # pip install pandas

# pip list (comando para listar paquetes instalados)
# pip uninstall pandas (desinstala paquete 'pandas')
# pip show numpy (muestra información de 'numpy')

# Requests: biblioteca esencial para trabajar con HTTP
# pip install requests
import requests # paquete para hacer peticiones a una API

# Petición GET
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response)

# Ver el código de estado
print(response.status_code)

# Ver el contenido de la respuesta
print(response.status_code)

# Trabajar con JSON
print(response.json())

# Arithetics Package (paquete personalizado que hemos creado)
# Desde los módulos importamos funciones

from mypackage import arithmetics # Importamos del archivo mypackage/arithmetics.py

print(arithmetics.sum_two_values(1, 4))
