### Modules ###

# import my_module # Importamos 'module.py'

# my_module.sum(5, 3, 1) # Para aceder a la función 'sum' primero hay que escribir 'my_module'
# my_module.printValue("Hola Python!")

from my_module import sumValue, printValue

sumValue(5, 3, 1) # Al importar función concreta basta con escribir la función 'sum'
printValue("Hola Python!")

import math # 'math' es un módulo que ofrece python

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE # con 'as' podemos renombrar propiedades de un módulo
