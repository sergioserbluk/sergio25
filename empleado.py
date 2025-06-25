nomina=[]
while True:
    res=input("quiere cargar un empleado? s/n:  ")
    if res=="s":
        hijos=[]
        nombre=input("ingrese el nombre: ")
        apellido=input("ingrese el apellido: ")
        dni=int(input("ingrese el dni: "))
        anac=int(input("ingrese el año de nacimiento "))
        resp=input("cargar un hijo s/n: ")
        while resp=="s":
            nhijo=input("ingrese el nombre del hijo: ")
            hijos.append(nhijo)
            resp=input("quiere cargar otro hijo s/n: ")
        nomina.append([nombre,apellido,dni,anac,hijos])
    else:
        break
print(nomina)        