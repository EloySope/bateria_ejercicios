def longitud(lista_o_cadena):
    count = 0
    for elemento in lista_o_cadena:
        count += 1
    return count

cadena = "aula cirtual asata"
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("La longitud de la cadena", longitud(cadena))
print("La longitud de la lista", longitud(lista))