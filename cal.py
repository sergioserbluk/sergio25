def sumar(num1, num2):
    res=num1+num2
    return res
try:
    n1=int(input("ingrese un numero"))
except ValueError:
    print("no se puede convertir a entero")
    n1=0
    # raise ValueError("no se puede convertir a entero") #se lanza una excepcion si no se puede convertir a entero
n2=int(input("ingrese otro numero"))
op = input("ingrese la operacion deseada: +, -, * o /")
if op=="+":
    # r=n1+n2
    r=sumar(n1,n2)
elif op=="-":
    r=n1-n2
elif op=="*":
    r=n1*n2
elif op=="/":
    try:
        r=n1/n2
    except ZeroDivisionError:
        print("no se puede dividir por cero...")
        r=None
print(f"el resultado de {n1} {op} {n2} es: {r}")
