#creo una lista de diez numeros aleatorios
import random
def creaLista():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 100))
    return lista
numeros = creaLista()
print(numeros)



for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print(numeros)

i=0
while i < len(numeros):
    j = i + 1
    while j < len(numeros):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
        j += 1
    i += 1