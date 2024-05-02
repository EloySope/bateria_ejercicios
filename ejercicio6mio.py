def funcion_sin_argumentos():
    print("Sin argumentos")

def funcion_con_argumento(argumento):
    print("El argumento es:" , argumento)

def cont_strings(arg1 , arg2 ,arg3):
    return arg1 + arg2 + arg3

resultado_1 = funcion_sin_argumentos()
print("Resultado primer punto: " , resultado_1)

resultado_2 = funcion_con_argumento("Buenas")
print("Resultado segundo punto: " , resultado_2)

resultado_3 = cont_strings("Buenas" , "tardes" , "señor")
print("Resultado tercer punto: " , resultado_3)