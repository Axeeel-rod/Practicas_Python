calificaciones = []
def datos():
    alumno = input("Ingresa el nombre del alumno: ").capitalize()
    if alumno == "":
        print("Debes ingresar el nombre del Alumno")
        return menu
    while True:
        try:
            numCalificaciones = int(input("Cuantas calificaciones desea agregar: "))
        except ValueError:
            print("Debes introducir la cantidad de calificaciones a ingresar")
            break
        suma = 0
        for i in range(numCalificaciones):
            try:
                calificacion = float(input(f"Ingrese la calificacion {i + 1} de {alumno} "))
            except ValueError:
                print("Debes introducir las calificaciones del Alumno")
                suma += calificacion
                promedio = suma / numCalificaciones
                calificaciones.append((alumno, promedio))

def alumnos():
    if not calificaciones:
        print("No hay Alumnos registrados")
    else:
        for alumno, promedio, in calificaciones:
            print(f"Alumno: {alumno}, Promedio: {promedio} ")

def menu():
    while True:
        print("---MENU---")
        print("(1)Ingresar un nuevo alumno\n(2)Ver los alumnos y los promedios\n(S)Salir")
        opcion = input("Ingresa una opcion: ")
        if opcion >= "3":
            print("Esa opcion es incorrecta")
        elif opcion == "1":
            datos()
        elif opcion == "2":
            alumnos()
            continue
        else:
            opcion == "S"
            decision= input("¿Seguro que desas finalizar el programa?\nSi/No: ").capitalize()
            if decision == "Si":
                exit()
            else:
                continue

menu()

