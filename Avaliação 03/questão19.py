'19. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os'
'demais elementos. Escreva ao ﬁnal a matriz obtida.'

Matriz = []
MatrizB = []
for l in range (5): #linhas
    for c in range (5): #colunas
        if c == l:
            MatrizB.append(1)
        else:
            MatrizB.append(0)
    Matriz.append(MatrizB)
    MatrizB = []
for i in range(len(Matriz)):
    print(Matriz[i])
    
