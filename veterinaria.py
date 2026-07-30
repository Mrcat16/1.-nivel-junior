
ficha_mascota = {
    "nombre": "oreo",
    "especie": "perro",
    "raza": "doberman",
    "edad": 4,
    "vacunas": ("Rabia", "Parvorirus")
}
sintomas_observados = []
def ver_ficha_y_vacuna():
    print()
    print("Ficha de la mascota:")
    print(f"Nombre: {ficha_mascota["nombre"]}")
    print(f"Especie: {ficha_mascota["especie"]}")
    print(f"Raza: {ficha_mascota["raza"]}")
    print(f"Edad: {ficha_mascota["edad"]} años")
    print()
    print("Vacunas que tiene tu perro:")
    for i, x in enumerate (ficha_mascota["vacunas"],1):
        print(f"{i},{x}")
def registrar_sintoma():
    print()
    sintoma = input("Que sintoma tiene su perro?: ").title().strip()
    if sintoma in sintomas_observados:
        print("El sintoma ya esta registrado:")
    else:
        sintomas_observados.append(sintoma)
        print()
        print("Ël sintoma se acaba de registrar correctamente:")
        print()
def buscar_sintoma ():
    print()
    buscar = input("Ingrese el sintoma que tiene su perro?: ").title().strip()
    if buscar in ["Rabia",]:
        print()
        print("Sintoma peligroso detectado")
        print("Quedese donde esta que un recepcionista va a su posicion:")
        print()
    else:
        print()
        print("Su perro no tiene ningun sintoma peligroso:")
        print()
def generar_reporte():
    if len(sintomas_observados) == 0:
        print()
        print("Su perro no tiene ninguno sintoma:")
        print()
    else:
        sintomas_observados.sort()
        print()
        print("Sintomas que tiene su perro")
        for s, d in enumerate (sintomas_observados,1):
            print(f"{s}.{d}")
        print()
def salir():
    print("Seguro que desea salir del programa de la veterinaria?:")
    print("si para salir:")
    print("no para volver al programa")
    sali = input("").lower().strip()
    while sali not in ["si", "no"]:
        print("Error porfa solo seleccione si para salir y no para volver al programa")
        sali = input("").lower().strip()
    if sali == "si":
        print("Gracias por usar el programa de la veterinaria chao")
        return True
    else:
        print("Volviendo al programa de la veterinaria")
        return False
        
while True:
    print()
    print("1.Ver Ficha y Vacunas:")
    print("2.Registrar Sintoma:")
    print("3.Buscar Sintoma Clave:")
    print("4.Generar Reporte de Pre-Consulta:")
    print("5.Salir:")
    print()
    opcion = input("Elija una de las opciones que se le muestran en pantalla: ").strip()
    if opcion == "1":
        ver_ficha_y_vacuna()
    elif opcion == "2":
        registrar_sintoma()
    elif opcion == "3":
        buscar_sintoma()
    elif opcion == "4":
        generar_reporte()
    elif opcion == "5":
        debe_cerrar = salir()
        if debe_cerrar:
            break
    else:
        print("Opcion no valida")