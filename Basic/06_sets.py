### Sets ### (De base es un array)

my_set = set()
my_other_set = {} # Con {} es un diccionario, no un set

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) # Vuelve a ser un set

print(len(my_other_set))

my_other_set.add("MoureDev") # Añade "MoureDev" de forma desordenada. Por lo tanto, un set no es una estructura ordenada
print(my_other_set)

my_other_set.add("MoureDev") # Un set no admite repetidos
print(my_other_set)

print("Moure" in my_other_set) # True
print("Mouri" in my_other_set) # False

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear() # Borra todos los elementos del set
print(len(my_other_set)) # 0

del my_other_set
#print(my_other_set) # Imprime error " my_other_set is not defined""

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # Ignora los 2 primeros union

print(my_new_set.difference(my_set))
