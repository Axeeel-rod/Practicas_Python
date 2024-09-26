Personas = []
def cargar_contactos():
    try:
        with open("agenda.txt", "r") as f_lectura:
            for linea in f_lectura:
                datos = linea.strip().split()
                nombre = datos[0]
                apellido = datos[1]
                edad = int(datos[3])  
                correo = datos[5]
                telefono = int(datos[7])  
                Personas.append([nombre, apellido, edad, correo, telefono])
    except FileNotFoundError:
        print("No hay contactos guardados todavía.")

cargar_contactos()

while True:
    print("""
    1.- Ingresar una persona a la agenda
    2.- Guardar agenda
    3.- Mostrar contactos
    4.- Editar un contacto 
    5.- Salir
          """)
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        contacto = []
        while True:
            nombre = input("Introduce tu nombre: ")
            apellido = input("Introduce tu apellido: ")
            if nombre == "":
                print("No has introducido tu nombre")
            elif apellido == "":
                print("No has introducido tu apellido")
            else:
                contacto.append(nombre)
                contacto.append(apellido)
                break

        while True:
            try:
                edad = int(input("Introduce tu edad: "))
                contacto.append(edad)
                break
            except ValueError:
                print("Debes introducir un número")

        correo = input("Introduce tu correo (Opcional): ")
        contacto.append(correo)
        while True:
            try: 
                telefono = int(input("Ingresa tu número de teléfono: "))
                contacto.append(telefono)
                break
            except ValueError:
                print("Debes ingresar un número válido")
        Personas.append(contacto)

    elif opcion == "2":
        with open("agenda.txt", "w") as f_agenda:
            for persona in Personas:
                f_agenda.write(f"{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n")
            print("Los datos se han guardado en Agenda.txt")
                
    elif opcion == "3":
        with open("agenda.txt", "r") as f_lectura:
            contenido = f_lectura.read()
            print(contenido)
    
    elif opcion == "4":
        if len(Personas) == 0:
            print("No hay contactos guardados")
        else:
            print("Contactos:")
            for i, persona in enumerate(Personas):
                print(f"{i}. {persona[0]} {persona[1]} - Edad: {persona[2]} Correo: {persona[3]} Teléfono: {persona[4]}")

            try:
                indice = int(input("Ingresa el número de contacto que quieres editar: "))
                if 0 <= indice < len(Personas):
                    contacto = Personas[indice]

                    nuevo_nombre = input(f"El nombre actual es: ({contacto[0]}), Presiona Enter para mantenerlo: ")
                    nuevo_apellido = input(f"El apellido actual es: ({contacto[1]}), Presiona Enter para mantenerlo: ")

                    try:
                        nueva_edad = input(f"La edad actual es: ({contacto[2]}), Presiona Enter para mantenerla: ")
                        if nueva_edad:
                            nueva_edad = int(nueva_edad)
                    except ValueError:
                        print("Edad inválida, se mantendrá la edad actual")
                    
                    nuevo_correo = input(f"El correo actual es: ({contacto[3]}), Presiona Enter para mantenerlo: ")
                    try:
                        nuevo_telefono = input(f"El teléfono actual es: ({contacto[4]}), Presiona Enter para mantenerlo: ")
                        if nuevo_telefono:
                            nuevo_telefono = int(nuevo_telefono)
                    except ValueError:
                        print("Debes ingresar un número de teléfono válido, se mantendrá el número actual.")

                   
                    if nuevo_nombre:
                        contacto[0] = nuevo_nombre
                    if nuevo_apellido:
                        contacto[1] = nuevo_apellido
                    if nueva_edad:
                        contacto[2] = nueva_edad
                    if nuevo_correo:
                        contacto[3] = nuevo_correo
                    if nuevo_telefono:
                        contacto[4] = nuevo_telefono

                    print("Datos actualizados correctamente")
                else:
                    print("Número de contacto inválido")
            except ValueError:
                print("Debes ingresar un número válido")
    elif opcion == "5":
        print("Salliendo del programa")
        break

                 


    
