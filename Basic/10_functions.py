### Functions ###

def my_function():
  print("Esto es una función")

my_function()

def sum_two_values(first_value, second_value):
  print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values("5","7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
  return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
  print(f"{name} {surname}")

print_name(surname = "Moure", name = "Brais")

def print_name_with_default(name, surname, alias = "Sin alias"): # Con '=' se asigna un valor por defecto en caso de que el usuario no introduzca parámetro
  print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure", "MoureDev")

def print_texts(*text): # '*' permite meter los parámetros que quiera el usuario
  print(text)

print_texts("Hola", "Python", "MoureDev") # Pase de parámetros por separado
