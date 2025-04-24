### Challenges ###

"""
  EL FAMOSO "FIZZ BUZZ"
  Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
  for i in range(1, 101): # Rango entre números 1 y 100
    if i % 3 == 0 and i % 5 == 0:
      print("fizzbuzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")
    else:
      print(i)

fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando
    TODAS las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""

def es_anagrama(palabra1, palabra2):
  if palabra1.lower() == palabra2.lower():
    return False
  return sorted(palabra1.lower()) == sorted(palabra2.lower()) # 'sorted' ordena alfabéticamente la cadena 'palabra1'

print(es_anagrama("losa", "sola"))


"""
Escribe un programa que imprima los 50 primeros números de la
    sucesión de Fibonacci empezando en 0.
    - La serie Fibonacci se compone por una sucesión de números en
     la que el siguiente siempre es la suma de los dos anteriores.
     0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
  num1 = 0
  num2 = 1

  for _ in range(0, 50):
    print(f"{num1}, ")
    suma = num1 + num2
    num1 = num2
    num2 = suma

fibonacci()

# Para que el resultado se imprima en una única línea de números separados por comas:

def fibonacci_una_linea():
  previo = 0
  siguiente = 1
  resultado = []

  for _ in range(50):
    resultado.append(str(previo))
    suma = previo + siguiente
    previo = siguiente
    siguiente = suma

  print(", ".join(resultado))

fibonacci_una_linea()

"""
ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(num):
  if num < 2:
    return False

  for i in range(2, num): #Comprueba hasta 'num' - 1
    if num % i == 0: #Si esta comprobación se cumple no es primo
      return False

  return True

print(es_primo(4))

for i in range(1, 101):
  if es_primo(i):
    print(i, end=", ")

print("")

"""
 INVIRTIENDO CADENAS
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invierte_orden(texto):
  resultado = ""
  longitud_texto = len(texto)

  for i in range(0, longitud_texto):
    resultado +=  texto[longitud_texto - i - 1] # Restamos 1 para que no se pase

  return resultado

print(invierte_orden("Hola mundo"))
