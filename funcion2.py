# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
# un carácter como segundo y otro carácter  como tercero,  
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter 
# en la cadena

import re


def reemplazarCaracteres(cadena:str,caracter1:str,caracter2:str)->str:
    contador = 0 
    lista_caracteres = []
    for caracter in cadena:
        if re.match(caracter1,caracter):
            contador += 1
            caracter = caracter2
            lista_caracteres.append(caracter)
        else:
            caracter = ""
            lista_caracteres.append(caracter)    
            
    lista_caracteres.join()    
    print(lista_caracteres)
    print(contador)
    
reemplazarCaracteres("Esto es una prueba","e","l")