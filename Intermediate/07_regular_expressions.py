### Regular expressions ###

import re # Importar módulo

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I) # 're.I' ignora mayúsculas y minúsculas
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
if not(match == None):
  print(match)
  start, end = match.span()
  print(my_other_string[start:end])


print(re.match("Esta es la lección", my_other_string))
# print(re.match("Expresiones Regulares", my_string))


# search

search = re.search("Esta es la lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


# findall

findall = re.findall("lección", my_string, re.I)
print(findall)


# split

print(re.split(":", my_string)) # 'split' busca un patrón y divide a partir de ahí


# sub

print(re.sub("[L|l]ección", "LECCIÓN", my_string)) # 'sub' sirve para sustituir p.e. mayúcula por minúscula
print(re.sub("Expresiones", "RegEx", my_string))


# Patterns
# Para aprender y validar expresiones regulares. https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[Ll]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$" # mientras tengamos el ., el $ nos va a tener en cuenta todo lo que aparezca después
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.es.mx"
print(re.findall(pattern, email))
