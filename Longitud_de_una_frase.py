palabra = input("Ingresa uuna palabra que contenga entre 4 y 8 letras: ")
if 4 <= len(palabra) <= 8:
    print("Palabra correcta")
elif len(palabra) < 4:
    print("Hacen falta letras, Solo tiene:", 8 - len(palabra), "Caracteres")
else:
    len(palabra) >8
    print("Sobran letras, Tiene:", len(palabra) - 8, "Caracteres de mas.")

