from funciones_p import *


while True:
    print("MENÚ CONTACTOS")
    print("1. Agregar contacto\n2. Mostrar contactos\n3. Guardar archivo CSV\n4. Salir")
    opc = int(input("Ingrese opción: "))
    if opc == 1:
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc == 3:
        opcion_3()
    else:
        opcion_4 