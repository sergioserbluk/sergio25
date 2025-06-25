#para ocultar el password uso la funcion getpass
from getpass import getpass
nus=input("ingrese su usuario: ")
pas=getpass("ingrese su contraseña: ")
while nus != "admin" or pas !="123":
    print("usuario o contraseña incorrectos! ")
    nus=input("ingrese su usuario: ")
    pas=getpass("ingrese su contraseña: ")
print("has podido ingresar! ")