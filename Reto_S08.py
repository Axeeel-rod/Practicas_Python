traductorEsp = {"rojo": "red",  "amarrilo": "yellow", "naranja": "orange", "verde": "green", "azul": "blue", "violeta": "violet" }  
traductorIng = {"red": "rojo",  "yellow": "amarillo", "orange": "naranja", "green": "verde", "blue": "azul", "violet": "violeta"}

opcion = input("Selecciona el idioma:\nEspañol(1)\nIngles(2)\nOpcion: ")

if opcion == "1":
    fraseEsp = input("Ingresa los colores en Español a traducir: ")
    fraseEsp = fraseEsp.lower()
    palabrasEsp = fraseEsp.split()
    entradaEsp = " "
    for palabrasEsp in palabrasEsp:
        if palabrasEsp in traductorEsp:
            entradaEsp = entradaEsp + traductorEsp[palabrasEsp] + " "
        else:
            entradaEsp = entradaEsp + palabrasEsp + " "
    print("Traduccion Español a Ingles:", entradaEsp.strip())

elif opcion == "2" :
    fraseIng = input("Ingresa los colores en Ingles a traducir: ")
    fraseIng = fraseIng.lower()
    palabrasIng = fraseIng.split()
    entradaIng = " "
    for palabrasIng in palabrasIng:
        if palabrasIng in traductorIng:
            entradaIng = entradaIng + traductorIng[palabrasIng] + " "
        else:
            entradaIng = entradaIng + palabrasIng + " "
    print("Traduccion Ingles a Español:", entradaIng.strip())
