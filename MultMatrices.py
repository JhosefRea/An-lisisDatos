
matriz = []
matriz2 = []
matriz3 = []

print("Ingrese datos de Primera Matriz")
fila = int(input("Ingrese el número de filas: "))
col = int(input("Ingrese el número de columnas: ")) 

for i in range(fila):
    matriz.append([])
    for j in range(col):
        elemento = float(input("Ingrese el número: "))
        matriz[i].append(elemento)  

print("\n\nIngrese datos de la Segunda Matriz")
fila = int(input("Ingrese el número de filas: "))
col = int(input("Ingrese el número de columnas: "))

for i in range(fila):
    matriz2.append([])
    for j in range(col):
        elemento = float(input("Ingrese el número: "))
        matriz2[i].append(elemento)  
    
    

if len(matriz[0]) == len(matriz2):

    for i in range(len(matriz)):
        matriz3.append([])
        for j in range(len(matriz2[0])):
            matriz3[i].append(0)


    for i in range(len(matriz)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz[0])):
                matriz3[i][j] += matriz[i][k] * matriz2[k][j] 

    print("Matrices ingresadas\n")
    for i in matriz:
        print("[", end= " ")
        for j in i:
            print(j, end=" ")
        print("]")  
    print("\n")
    for i in matriz:
        print("[", end= " ")
        for j in i:
            print(j, end=" ")
        print("]")        

    print("\n-----------------------")
    print("Matriz de multiplicación: ")
    for i in matriz3:
        print("[", end= " ")
        for j in i:
            print(j, end=" ")
        print("]")    
     
else:
    print("No se puede realizar la multiplicación")     