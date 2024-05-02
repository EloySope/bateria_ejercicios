alfabeto_numeros = {"A" : 1 , "B" : 2 , "C" : 3 , "D" : 4 , "E" : 5 , "F" : 6 , "G" : 7 , "H" : 8 , "I" : 9 , "J" : 10 }

print(alfabeto_numeros["c"])

alfabeto_numeros2 = dict()

for key in alfabeto_numeros:
    alfabeto_numeros2[key.lower()] = alfabeto_numeros[key]

print(alfabeto_numeros2)