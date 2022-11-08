matrizA = []
matrizB = []
matrizC = []

for i in range(4):
    matrizA.append([0]*4)
    matrizB.append([0]*4)
    matrizC.append([0]*4)

for x in range(2):
    for i in range(4):
        for j in range(4):
            elemento = int(input(f"Matriz {x+1}: Posição:{i}x{j}:"))

            if (x == 0):
                matrizA[i][j] = elemento       
            else:
                if (x == 1):
                    matrizB[i][j] = elemento

for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
        if matrizA[i][j] > matrizB[i][j]:
            matrizC[i][j] = matrizA[i][j]
        else:
            matrizC[i][j] = matrizB[i][j]

    print(matrizC[i])