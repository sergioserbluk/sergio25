import random
import os
ci=0
while True:
    try: 
        nus=int(input("ingrese un numero entre 1 y 100: "))
        break
    except ValueError:
        print("eso no es un numero entero. intentelo de nuevo.")
    os.system("cls")
while True:
    npc=random.randint(1,100)
    ci=ci+1
    if npc==nus:
        print("el numero que pensaste es: ", npc)
        print("lo encontre en ", ci, "intentos")
        break
