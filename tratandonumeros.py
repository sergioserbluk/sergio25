while True:
    try:
        numero = int(input("Introduce un número: "))
        break
    except ValueError:
        print("Eso no es un número entero. Inténtalo de nuevo.")