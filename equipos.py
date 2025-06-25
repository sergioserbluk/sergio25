equipos = {
    "Boca Juniors": {
        "localidad": "La Boca",
        "provincia": "Ciudad Autónoma de Buenos Aires",
        "categoria": "Primera División"
    },
    "River Plate": {
        "localidad": "Núñez",
        "provincia": "Ciudad Autónoma de Buenos Aires",
        "categoria": "Primera División"
    },
    "Independiente": {
        "localidad": "Avellaneda",
        "provincia": "Buenos Aires",
        "categoria": "Primera División"
    },
    "Racing Club": {
        "localidad": "Avellaneda",
        "provincia": "Buenos Aires",
        "categoria": "Primera División"
    },
    "San Lorenzo": {
        "localidad": "Boedo",
        "provincia": "Ciudad Autónoma de Buenos Aires",
        "categoria": "Primera División"
    },
    "Huracán": {
        "localidad": "Parque Patricios",
        "provincia": "Ciudad Autónoma de Buenos Aires",
        "categoria": "Primera División"
    },
    "Rosario Central": {
        "localidad": "Rosario",
        "provincia": "Santa Fe",
        "categoria": "Primera División"
    },
    "Newell's Old Boys": {
        "localidad": "Rosario",
        "provincia": "Santa Fe",
        "categoria": "Primera División"
    },
    "Talleres": {
        "localidad": "Córdoba",
        "provincia": "Córdoba",
        "categoria": "Primera División"
    },
    "Belgrano": {
        "localidad": "Córdoba",
        "provincia": "Córdoba",
        "categoria": "Primera División"
    },
    "Gimnasia y Esgrima La Plata": {
        "localidad": "La Plata",
        "provincia": "Buenos Aires",
        "categoria": "Primera División"
    },
    "Estudiantes de La Plata": {
        "localidad": "La Plata",
        "provincia": "Buenos Aires",
        "categoria": "Primera División"
    },
    "Argentinos Juniors": {
        "localidad": "La Paternal",
        "provincia": "Ciudad Autónoma de Buenos Aires",
        "categoria": "Primera División"
    },
    "Instituto": {
        "localidad": "Córdoba",
        "provincia": "Córdoba",
        "categoria": "Primera División"
    },
    "Chacarita Juniors": {
        "localidad": "Villa Maipú",
        "provincia": "Buenos Aires",
        "categoria": "Primera Nacional"
    }
}
#recorro el diccionario por claves
print("Equipos y sus datos:")
for equipo in equipos:
    print(f"Equipo: {equipo}")
    print(f"Localidad: {equipos[equipo]['localidad']}")
    print(f"Provincia: {equipos[equipo]['provincia']}")
    print(f"Categoría: {equipos[equipo]['categoria']}")
    print()  # Línea en blanco para mejor legibilidad
#recorro el diccionario por items
print("Equipos y sus datos:")
for equipo, datos in equipos.items():
    print(f"Equipo: {equipo}")
    print(f"Localidad: {datos['localidad']}")
    print(f"Provincia: {datos['provincia']}")
    print(f"Categoría: {datos['categoria']}")
    print()  # Línea en blanco para mejor legibilidad
#recorro el diccionario por valores
print("Equipos y sus datos:")
for datos in equipos.values():
    print(f"Localidad: {datos['localidad']}")
    print(f"Provincia: {datos['provincia']}")
    print(f"Categoría: {datos['categoria']}")
    print()  # Línea en blanco para mejor legibilidad

    


