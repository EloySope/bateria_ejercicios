def sum(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def multip(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

# Ejemplos de uso:
lista = [1, 2, 3, 4]
print("Suma:", sum(lista))
print("Multiplicación:", multip(lista))