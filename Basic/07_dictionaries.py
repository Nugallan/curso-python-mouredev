### Dictionaries ###
#Tipo de estructura que podemos almacenar datos clave-valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"} # Relación clave - valor
my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes": {"Python","Swift","Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5

print(my_dict["Nombre"]) # Ventaja de 'diccionarios': facilidad para acceder a elementos

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1]) # 1.77

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

del (my_dict["Calle"]) # Forma para eliminar un elemento en un 'diccionario'
print(my_dict)

print("Moure" in my_dict) # False -> porque busca por clave, no por valor
print("Mouri" in my_dict) # False
print("Apellido" in my_dict) # True

print(my_dict.items()) # Listado con cada uno de los items
print(my_dict.keys()) # Muestra una lista de las claves
print(my_dict.values()) # Muestra una lista de los valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Crea un diccionario
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Moure")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
