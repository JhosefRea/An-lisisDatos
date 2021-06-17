import re as noContar

diccionario = {}
palabras = []

print("Número de ocurrencias de cada palabra de un txt\n")
archivo = open('ZlatanIbra.txt',encoding='utf8')

texto = archivo.readline()

while texto != "":
    palabras = texto.split()

    for i in range(len(palabras)):
        palabra = noContar.sub('[?|.|!|\/|;|:|,|”|“|(|)]' , '', palabras[i])
        #Elimina caracteres no deseados
    
        if palabra in diccionario:#revisa si existe la palabra
            diccionario[palabra] += 1#añade una ocurrencia
        else:
            diccionario.update({palabra:1})
    texto = archivo.readline()

archivo.close()

print("Número de ocurrencias de cada palabra o número: ")

for i in diccionario:#recorrer el diccionario
    print('({},{}) '.format(i,diccionario.get(i))) #formato (palabra, ocurrencia)

