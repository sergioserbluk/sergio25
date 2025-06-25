#este algoritmo solicita al usuario una letra, a partir de se genera un numero aleatorio entre 1 y 23 inclusive
letra = input("Ingrese una letra: ") 
nombre = input("Ingrese su nombre: ")
#se crea una lista con las letras del abecedario
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
#se crea una lista con los numeros del abecedario
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
#se crea un diccionario con las letras del abecedario y su respectivo numero

import random
numero = random.randint(1,23)
#se crea un diccionario con las letras del abecedario y su respectivo numero
