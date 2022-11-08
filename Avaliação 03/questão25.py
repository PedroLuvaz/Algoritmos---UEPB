'Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão'
'na diagonal secundária.'

Matriz = []
MatrizB = []
soma = 0
for l in range (3): #linhas
    for c in range (3): #colunas
        Matrizvalor = int(input(f'Digite aqui o número {l}x{c}: '))
        MatrizB.append(Matrizvalor)#2x0 1x1 0x2 
        if l+c == 2:
            soma += Matrizvalor 
    Matriz.append(MatrizB)
    MatrizB = []        
for i in range(len(Matriz)):
    print(Matriz[i])
print(f'A sua soma foi de: {soma}')