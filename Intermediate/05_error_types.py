### Error types ###

# Syntax error
# print "¡Hola comunidad!" # Descomentar para error Error
print("¡Hola comunidad!")


# NameError
language = "Spanish" # Comentar para error
print(language)


# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[4])
#print(my_list[5]) # Descomentar para error


# ModuleNotFoundError
# import maths # Descomentar para error


# AttributeError
import math
# print(math.PI) # (mal escrito en mayus) Descomentar para error


#KeyError
my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad": 35, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para error


# TypeError
#print(my_list["Nombre"]) # Descomentar para error
print(my_list[0])


# ImportError
#from math import PI # Descomentar para error
#print(pi) # Descomentar para error


# ValueError
#my_int = "10" # Descomentar para error
#print(type(my_int))


# ZeroDivisionError
#print(4/0) # Descomentar para error
print(4/2)

