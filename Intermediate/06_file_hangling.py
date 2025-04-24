### File Hangling ###

import os
from turtle import width

# .txt file

txt_file = open("Intermediate/my_file.txt", "w+") # Leer y Escribir

txt_file.write("\nAunque también me gusta Kotlin")

print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())

for line in txt_file.readlines():
  print(line)

txt_file.write("\nAunque también me gusta Kotlin")
# print(txt_file.readLine())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
  my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")


# .json file

import json

json_file = open("Intermediate/my_file.json", "w+") # Crea el fichero desde 0

json_text = {
  "name":"Brais",
  "surname":"Moure",
  "age":35,
  "language":["Python","Swift","Kotlin"],
  "website":"https://moure.dev"
}

json.dump(json_text, json_file, indent = 4) # 'indent' genera 4 espacios con un tipo de formato asignado por el número para el código json

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
  for line in my_other_file.readlines():
    print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


# .csv file
import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
  for line in my_other_file.readlines():
    print(line)


# .xlsx file
# import xlrd # Debe instalarse el módulo


# .xml fil
# import xml
