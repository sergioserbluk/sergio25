n=80
while n>50:
    n=int(input("ingrese un numero: "))
    if n>50:
        print("el numero es mayor a 50")
print("usted ingreso: ", n)

print ("usando range")
while True:
    n=int(input("ingrese un numero: "))
    if n in range(0,50):
        break
    else:
        print("el numero es mayor a 50")
print("usted ingreso: ", n)