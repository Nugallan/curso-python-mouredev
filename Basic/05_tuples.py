### Tuples: conjunto de valores (no son listas) ###

# 2 formas de definir tuplas:
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80
# my_tuple[5] = 1.80
# print(my_tuple) # Da error, ya que las tuplas son inmutables

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # La suma de tuplas está permitida

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Conversión de la tupla a lista
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
