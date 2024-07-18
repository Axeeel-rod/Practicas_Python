def crearContraseña ():
    print("*** Crea una contraseña que empiece con un numero ***")

for _ in range (3) :
        crearContraseña()

        contraseña1 = input ("Ingresa la contraseña:")
        contraseña2 = input ("Vuelve a ingresar la contraseña:")

        if not contraseña1[0].isdigit():
            print("La contraseña debe iniciar con un numero")
            continue
  
        intentos = 3

        while intentos > 0 :
            if contraseña1 == contraseña2 :
                print("Contraseña correcta")
                exit()

            else:
                 print(f"Contraseña incorrecta, Intenta de nuevo te quedan {intentos - 1} intentos.")
                 break
        contraseña1 = input("Ingresa la contraseña:") 
        contraseña2 = input("Vuelve a ingresar la contraseña:")
        intentos -= 1
        if contraseña1 == contraseña2 :
             print("Contraseña correcta")
             exit()


 
     
     

 


  
  



    















     
    
     



    
    










