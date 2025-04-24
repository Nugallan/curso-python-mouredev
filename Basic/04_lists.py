### Lists (Arrays) ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # Imprime la última posición de la lista
print(my_other_list[-4])
print(my_list.count(30)) # Imprime '2' que son las veces que se repite el elemento '30'
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list # Asignación de valores a las variables según posición en lista
print(name)

name, height, age, surname = my_other_list
print(name) # Ahora la variable 'name' imprime 35 al ser la primera posición de la lista

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list) # Imprime una nueva lista uniendo primero los valores de 'my_list' y a continuación 'my_other_list'

my_other_list.append("MoureDev") # Lo añade como valor final a la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Añade "Rojo" en la posición 1
print(my_other_list)

my_other_list[1] = "Azul" # Antes era rojo y lo sustituimos directamente por "Azul"
print(my_other_list)

my_list.remove(30) # Elimina el valor '30' de la lista
print(my_other_list)

del my_list[2] # Elimina el elemento de la posición 2
print(my_list)

my_other_list.pop() # Elimina por defecto el último valor de la lista
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # Ordena de menor a mayor
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))
