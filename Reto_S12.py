import matplotlib.pyplot as plt 

año_inicial = int(input("Ingresa el año inicial de la ventas: "))
año_final = int(input("Ingresa el ultimo año de las ventas: "))

ventas = []
años = list(range( año_inicial, año_final + 1))
for año in años: 
    venta = float(input(f"Ingresa el monto de las ventas para el año {año}: "))
    ventas.append (venta)

plt.plot(años, ventas, marker = "o", linestyle = "-", color = "blue")
plt.title ("Grafica de ventas")
plt.xlabel("años")
plt.ylabel("ventas")
plt.show()






    
 



