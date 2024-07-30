import random
lista_nombres = ["Axel","Fatima","Lety","Jesus","Yetzi","Nathaly"]
nombre_secreto = random.choice(lista_nombres)
numero_intentos = 3
while numero_intentos > 0:
    resultado = input("Dime en quien estoy pensando: ")
    if resultado == nombre_secreto:
        print("Ganaste!!")
        break
    else:
        print("Te quedan,", numero_intentos -1 ,"intento")
        numero_intentos -=1
   
