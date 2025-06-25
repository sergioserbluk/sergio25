estaturas=[]
for x in range(5):
    est=float(input("ingrese una estatura: "))
    estaturas.append(est)
sumatoria=0
for x in estaturas:
    sumatoria=sumatoria+x
promedio=sumatoria/len(estaturas)
print(f"el promedio de estaturas es {promedio}")
estaturas.sort()
print(f"la estatura menor es {estaturas[0]}")
print(f"la estatura mayor es {estaturas[len(estaturas)-1]}")