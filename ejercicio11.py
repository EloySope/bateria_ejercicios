"""
def procedimiento(lista):
    for num in lista:
        print("*" * num)

procedimiento([5 , 12 , 6])
"""

from ejercicio10 import generar_n_caracteres

def procedimiento(lista):
    for num in lista:
        print(generar_n_caracteres(num , "*"))

procedimiento([12 , 3 , 5])