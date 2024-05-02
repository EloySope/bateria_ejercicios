
def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales


caracter_ejemplo = "j"
var_vocal_flag = es_vocal(caracter_ejemplo)
print(var_vocal_flag)

