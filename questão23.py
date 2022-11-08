'Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão'
'acima da diagonal principal.'

Matriz = []
MatrizB = []
soma = 0
for l in range (3): #linhas
    for c in range (3): #colunas
        Matrizvalor = int(input(f'Digite aqui o número {l}x{c}: '))
        MatrizB.append(Matrizvalor)
        if l < c:                    
            soma += Matrizvalor
    Matriz.append(MatrizB)
    MatrizB = []
for i in range(len(Matriz)):
    print(Matriz[i])
print(f'A sua soma foi de: {soma}')