### Higher Order Functions ###

# Son funciones que "hacen cosas" con otras funciones (jerarquía de funciones)

def sum_one(value):
  return value + 1

def sum_five(value):
  return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum_one):
  return f_sum_one(first_value + second_value)

print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))


### Closures ###

def sum_ten(original_value):
  def add(value):
    return value + 10 + original_value
  return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 30]

# Map: recorre todos los valores y ejecuta una función sobre ellos para modificar su valor

def multiply_two(number):
  return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers))) # mismo ejemplo usando 'lambda'

# Filter: recorre todos los valores y ejecuta una función que retorna True o False para saber cómo filtrar los valores

def filter_greater_than_10(number):
  if number > 10:
    return True
  return False

print(list(filter(filter_greater_than_10, numbers)))
print(list(filter(lambda number: number > 10, numbers))) # mismo ejemplo usando 'lambda'


# Reduce: operar entre los valores que va recorriendo y va operando con los valores que va teniendo en cada caso a medida que vamos recorriendo este iterable

from functools import reduce # Para usar 'reduce' hay que importar de 'functools'

# numbers = [2, 5, 10, 21, 30]

def sum_two_values(first_value, second_value):
  print(first_value)
  print(second_value)
  return first_value + second_value

print(reduce(sum_two_values, numbers)) # 'Reduce' opera con un valor más el acumulador
