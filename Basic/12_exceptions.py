### Exceptions ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try / except

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except:
  print("Se ha producido un error")

# try / except / else

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except: # 'except' es obligatorio
  print("Se ha producido un error")
else: # 'else' es opcional
  # Se ejecuta si no se produce una excepción
  print("La ejecución continúa correctamente")
finally: # 'finally' es opcional
  # Se ejecuta siempre
  print("La ejecución continúa")


# Excepciones por tipo

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except ValueError:
  print("Se ha producido un ValueError")
except TypeError:
  print("Se ha producido un TypeError")


#Captura de la información de la excepción

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except ValueError as error:
  print(error)
except Exception as exception: #Formar de controlar que sea el error que sea, el error se controle
  print(exception)
