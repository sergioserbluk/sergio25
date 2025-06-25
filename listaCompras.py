compras=[]
resp="s"
while resp == "s":
    elemento=input("ingrese el producto: ")
    compras.append(elemento)
    resp=input("quiere agregar otro elemento a la lista? s/n: ")
print(compras)