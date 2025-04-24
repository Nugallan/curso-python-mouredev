### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\Este es un String \\ escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
# 2 formas de formateo:
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Usando {} imprime tal cual el objeto
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age)) # Usando '%s' el primer texto que pase formateado a esta cadena de texto lo mete ahí
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Modo inferencia de datos
print("Mi nombre es " + name + " " + surname + " y miedad es " + str(age)) # Esta forma está desaconsejada

#Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] # Imprime 'yt'
print(language_slice)

language_slice = language[1:] # Imprime 'ython'
print(language_slice)

language_slice = language[-2] # Imprimer 'o'
print(language_slice)

language_slice = language[0:6:2] #Imprimer 'Pto'
print(language_slice)

#Reverse

reversed_language = language[::-1] # Imprime 'nohtyP'
print(reversed_language)

# Funciones
print('#Funciones')

print(language.capitalize()) #Primera letra mayúscula
print(language.upper()) # Toda la cadena en mayúscula
print(language.lower()) #Toda la cadena en minúscula
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric)
print(language.upper().isupper())
print(language.startswith("Py"))
