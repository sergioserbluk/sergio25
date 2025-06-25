#pido los datos que describen a una zapatilla para guardar en un diccionario
import json
def cargar_datos_zapatilla():
    zapatilla = {}
    zapatilla["marca"] = input("Ingrese la marca de la zapatilla: ")
    zapatilla["modelo"] = input("Ingrese el modelo de la zapatilla: ")
    zapatilla["talla"] = input("Ingrese la talla de la zapatilla: ")
    zapatilla["color"] = input("Ingrese el color de la zapatilla: ")
    return zapatilla

def guardar_datos_zapatilla(zapatilla):
    with open("zapatilla.json", "w") as archivo: # Abre el archivo en modo escritura si no existe lo crea
        json.dump(zapatilla, archivo, indent=4)  # Guarda el diccionario en formato JSON con una sangría de 4 espacios

def cargar_datos_zapatilla_desde_archivo():
    try:
        with open("zapatilla.json","r") as archivo: # Abre el archivo en modo lectura
            zapatilla = json.load(archivo)
            return zapatilla
    except FileNotFoundError:
        print("El archivo no existe. Asegúrese de que los datos estén guardados.")
        return None
def mostrar_datos_zapatilla(zapatilla):
    if zapatilla:
        print("Datos de la zapatilla:")
        for clave, valor in zapatilla.items():
            print(f"{clave}: {valor}")
    else:
        print("No hay datos de zapatilla para mostrar.")
def menu():
    while True:
        print("\nMenú:")
        print("1. Cargar datos de zapatilla")
        print("2. Guardar datos de zapatilla en archivo")
        print("3. Cargar datos de zapatilla desde archivo")
        print("4. Mostrar datos de zapatilla")
        print("5. Salir")   
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            zapatilla = cargar_datos_zapatilla()
        elif opcion == "2":
            guardar_datos_zapatilla(zapatilla)
        elif opcion == "3":
            zapatilla = cargar_datos_zapatilla_desde_archivo()
        elif opcion == "4":
            mostrar_datos_zapatilla(zapatilla)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
if __name__ == "__main__":
    menu()
