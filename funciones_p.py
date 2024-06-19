contactos = []

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = validar_nombre
    telefono = validar_telefono
    correo = validar_correo

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    contactos.append(contacto)
    print("contacto agregado!")

    

def opcion_2():
    if validar_contactos():
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE: {c['nombre']}")
            print(f"TELÉFONO: {c['telefono']}")
            print(f"CORREO: {c['correo']}\n")

def opcion_3():
   if validar_contactos():
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





############
    #validacion

def validar_opciones(lista_opciones):
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in lista_opciones:
                return opc
            else:
                print("ERROR! opción incorrecta ")
        except:
            print("ERROR! debe ingresar un número entero!")


def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre)>3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! el nombre debe tener al menos 3 letras ")


def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese teléfono: "))
            if len(str(telefono)) == 9 and str(telefono)[0]=='9':
                return telefono
            else:
                print("ERROR! el teléfono debe comenzar con 9 y tener 9 digitos!")

        except:
            print("ERROR! debe ingresar un número entero!")


def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if correo.lower().endswith("@gmail.com") and len(correo.strip())>=13:
            return correo
        else:
            print("ERROR! correo incorrecto")
#pattern ---> buscar
            

def validar_contactos():
    if len(contactos) == 0:
        print("no existen contactos, agregue usando la opción 1!")
        return False
    return True

