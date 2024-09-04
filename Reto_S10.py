def crear_listas():
    tamaño = int(input("Ingresa el tamaño de la lista: "))
    lista = []
    for i in range (tamaño):
        elementos = input(f"Ingrese el elemento {i + 1}: ")
        lista.append(elementos)
    return lista

def eliminacion(lista1, lista2):
    return [elementos for elementos in lista1 if elementos not in lista2]


print("Creacion de la primera lista")
lista1 = crear_listas()
print("Creacion de la segunda lista")
lista2 = crear_listas()

print ("Estas son las listas originales:")
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)

lista_corregida = eliminacion(lista1, lista2)
print("Lista despues de eliminar la diferencia con la segunta lista")
print("Lista corregida: ", lista_corregida )









