# 3. Crear una función que se llame ordenarCaracteres que reciba 
# una cadena de caracteres como parámetro  y su responsabilidad es ordenar 
# los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres(cadena:str) -> str:
    tam = len(cadena)
            
    for i in range(tam - 1):
        for j in range (i + 1, tam):
            if (cadena[i] > cadena[j]):  
                aux = cadena[i]
                cadena[i] = cadena[j]     
                cadena[j] = aux   
                
    print(cadena)
    

ordenarCaracteres("algoritmo")