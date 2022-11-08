'Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da'
'forma:'

Matriz = []
MatrizB = []
caso1 = 0
caso2 = 0
caso3 = 0
for l in range (10): #linhas
    for c in range (10): #colunas
        if c == l:
            caso2 = 3*(l**2) - 1
            MatrizB.append(caso2)
        else:
            if l < c:
                caso1 = (2*l) + (7*c) - 2
                MatrizB.append(caso1)
            else:
                if l > c:                           
                    caso3 = 4*(l**3) - 5*(c**2) + 1
                    MatrizB.append(caso3)
    Matriz.append(MatrizB)
    MatrizB = []
for i in range(len(Matriz)):
    print(Matriz[i])
