lista = [] 
alumnos = True

while alumnos:
    opcion = input("Ingresar un alumno (1)\nSalir del programa (2)\nIngrese una opcion: ")
    if  opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        print ("Debes ingresar una calificacion como minimo")
        calificacion1 = float(input(f"Ingrese la primera calificacion del alumno {nombre}: "))
        calificacion2 = float(input(f"Ingrese la segunda calificacion del alumno {nombre}: "))
        calificacion3 = float(input(f"Ingrese la tercera calificacion del alumno {nombre}: "))
        promedio = (calificacion1 + calificacion2 + calificacion3 ) /3 
        promedio_final = round(promedio, 1)
        alumno = [nombre, calificacion1, calificacion2, calificacion3, ("Promedio:",promedio_final)]
        lista.append(alumno)
        alumnos += 1
    elif opcion == "2":
        print(f"El programa a terminado con {alumnos} alumnos.")
        break
    else:
        print("Se ingreso una opcion no valida")
        continue
   
print("La lista de alumnos es:")
for sublistas in lista:
        print(sublistas)







