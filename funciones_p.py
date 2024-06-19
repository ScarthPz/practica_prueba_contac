contactos = []

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese nombre: ")
    telefono = int(input("Ingrese teléfono: "))
    correo = input("Ingrese correo: ")

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    contactos.append(contacto)
    print("contacto agregado!")

    

def opcion_2():
    if len(contactos) == 0:
        print("no existe contactos, primero agregue alguno en la opción 1")
    else:
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE: {c['nombre']}")
            print(f"TELÉFONO: {c['telefono']}")
            print(f"CORREO: {c['correo']}\n")

def opcion_3():
    if len(contactos) == 0:
        print("no existen contactos, primero agregue alguno en la opción 1!")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")
        import csv
        with open(nombre_archivo+".csv", "w", newline="") as archivo:
            escritor = csv.DictWriter(archivo, ["nombre", "telefono", "correo"])
            escritor.writeheader()
            escritor.writerows(contactos)
        print("archivo creado!")


def opcion_4():
    print("Adios!")
    exit()