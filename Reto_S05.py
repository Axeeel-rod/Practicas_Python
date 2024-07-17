entrada1 = input("Introduce el año actual: ")
year1 = int(entrada1) 

entrada2 = input("Introduce otro año para calcular: ")
year2 = int(entrada2)

if year1 == year2:
    print("Es el mismo año")

elif year1 > year2:
     años_pasados = year1 - year2
     print("Han pasado", años_pasados,"años.")
elif year1 < year2:
     años_futuros = year2 - year1
     print("Faltan",años_futuros," años para llegar al año que introduciste")





