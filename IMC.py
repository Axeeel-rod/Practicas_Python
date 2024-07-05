#Calculadora de Indice de Masa Corporal
nombre = input("Nombre: ")
apellido_pat = input("Apellido Paterno: ")
apellido_mat = input("Apelllido Materno: ")
edad = int(input("Introduce tu edad: "))
peso = float(input("Introduce tu peso: "))
estatura = float(input("Introduce tu estatura: "))

#Calculamos el IMC

imc = peso / estatura**2

#Imprimimos los datos 

print("Nombre: " + nombre)
print("Apellido paterno: " + apellido_pat)
print("Apellido materno: " + apellido_mat)
print("Edad: " + str(edad))
print("Peso: {:.2f}".format(peso))
print("Estatura: {:.2f}".format(estatura))
print("Tu IMC es: {:.4f}".format(imc))



