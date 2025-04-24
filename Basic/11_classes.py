### Classes ###

class MyEmptyPerson:
  pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
  # '__init__' palabra reservada para crear un constructor de clase
  def __init__(self, name, surname, alias = "sin alias"): # Es requerido llamar a 'self' (a sí mismo)
    self.name = name
    self.surname = surname
    self.alias = alias

  def get_name(self): # Amago de 'getter'
    return self.name

  def walk(self): # Importante obligatorio poner 'self' aquí
    print(f"{self.name} Está caminando")

my_person = Person("Brais", "Moure")
print(f"{my_person.name} {my_person.surname}")
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.name)
my_other_person.walk()
my_other_person.name = "Héctor de León El loco de los perros"
print(my_other_person.name)
