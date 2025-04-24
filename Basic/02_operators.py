### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(10 % 3)
print(10 // 3) # Floor division (aproxima a un número entero)
print(2 ** 3) # '**' Exponente

print("Hola" + "Python")
# print("Hola " + 5) # Error: no podemos mezclar un string con un int
print("Hola " + str(5)) # Imprime 5 veces 'hola'
print("Hola" * 5) # Imprime 5 veces 'hola'

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print("")
print ("Hola" > "Python")
print ("Hola" < "Python")
print ("Hola" >= ">Zola") # Ordenación alfabética
print ("Hola" <= "Python")
print ("Hola" == "Python")
print ("Hola" != "Python")

### Operadores Lógicos ###
print('### Operadores Lógicos ###')
print(3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" > "Python")
print (3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))
