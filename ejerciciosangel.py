# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:07:33 2020

@author: angel
"""

print ("BIENVENIDO A EMPAREJANDO.COM")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Dinos cuál es tu nombre ")

ano = int(input("Y ahora... dinos, ¿en qué año naciste? "))

taburete = input("Por último, la pregunta más importante,¿te gusta taburete? ")

edad = 2020-ano

print("Hola, "+nombre+". Si no me equivoco tienes",edad,"años.")

if (taburete=="Si"):
    print ("Okay boomer")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

contador=1


#Ejercicio 2

while (contador<edad):
    print("Que no cumple",contador)
    contador+=1

print("¡ Que sí cumple",contador,"!")

#Ejercicio 3

for contador in range(1,edad):
    print("Que no cumple",contador)

print("¡ Que sí cumple",edad,"!")

#Ejercicio 4

usuario=(nombre,edad,taburete)

for dato in usuario:
    print(dato)
    
#Ejercicio5

usuario={
        "nombre":nombre,
        "edad":edad,
        "taburete":taburete
        }

for dato in usuario.values():
    print(dato)

#Ejercicio 6

abecedario= ' abcdefghijklmnñopqrstuvwxyz '

print("Esto es mi cifrado César")

texto_claro=input("Escribe la frase que quieres descifrar: ")
clave=int(input("Para descifrar, elige un número(Un número del 1 al 27):"))



texto_cifrado=""


for letra in texto_claro:
    nueva_posicion=abecedario.find(letra)+ clave
    letra_cifrada=int(nueva_posicion)%len(abecedario)
    texto_cifrado= texto_cifrado+str(abecedario[letra_cifrada])
print ("El mensaje cifrado es:" ,texto_cifrado)
print ("=====================================================")   

#Ejercicio 7

texto_descifrado=""
for letra in texto_cifrado:
    nueva_posicion= abecedario.find(letra)-clave
    letra_cifrada= int(nueva_posicion)%len(abecedario)
    texto_descifrado= texto_descifrado+str(abecedario[letra_cifrada])
print ("El mensaje descifrado es: " ,texto_descifrado) 


