def letra_anterior_siguiente (letra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    letra = letra.lower()
    if letra not in alfabeto:
        return "No es una letra valiida"
    posicion = alfabeto.index(letra)
    anterior = alfabeto[posicion - 1] if posicion > 0 else alfabeto[-1]
    siguiente = alfabeto [posicion + 1] if posicion < len(alfabeto) - 1 else alfabeto[0]
    return (f"Letra anterior : {anterior}, Letra sigueinte: {siguiente}")

def main():
    print("Para salir escriba `Salir´.")

    while True:
        letra = input("Ingrese una letra del abecedario: ").strip()

        if letra.lower() == "salir":
            print("Saliendo del programa")
            break

        elif len(letra ) != 1 or not letra.isalpha():
            print("Ingresa una letra valida")
            continue
        resultado = letra_anterior_siguiente(letra)
        print(resultado)

if __name__ == "__main__":
    main()


    
