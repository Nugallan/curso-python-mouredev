### Loops ###

# While

my_condition = 0

while my_condition < 10:
  print(my_condition)
  my_condition += 2
else: # Este 'else' es opcional y pertenece al 'while'. Pocos lenguajes como python aceptan 'else' en un 'while'
  print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
  my_condition += 1
  if my_condition == 15:
    print("Se detiene la ejecución")
    break

  print(my_condition)

print("La ejecución continúa")


# For
print ("# For")
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
  print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
  print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
  print(element)

my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

for element in my_dict:
  print(element)
  if element == "Edad":
    continue # Es como un 'break' pero detiene en este punto y retoma el inicio del 'for'. No aconsejable su uso
  print("Se ejecuta")
else: # Uso opcional de 'else' al igual que antes en el 'while'
  print("El bucle for para diccionario ha finalizado")
