def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False


lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 2]                                                    

print(superposicion(lista1, lista2)) 