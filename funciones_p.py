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
    pass

def opcion_3():
    pass

def opcion_4():
    pass