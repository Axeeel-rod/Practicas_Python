coordenadas = []
coordenada1 = int(input("Ingresa un numero X: "))
coordenada2 = int(input("Ingresa un numero Y: "))

coordenadas.append(coordenada1)
coordenadas.append(coordenada2)

for cuadrantes in coordenadas:
    if  coordenada1 > 0  and coordenada2 > 0:
        print("Estas en elcuadrante I")
        break
    elif coordenada1 < 0 and coordenada2 > 0:
        print("Estas en el cuadrante II")
        break
    elif coordenada1 < 0 and coordenada2 < 0:
        print("Estas en el cuadrante III")
        break
    elif coordenada1 >0  and coordenada2 < 0:
        print("Estas en el cuadrante IV")
        break
    else:
        coordenada1 or coordenada2 == 0
        print("Las coordenas no pueden valer 0 ")
        break


    


    