'18. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela'
'possui.'

matrizA = []
matrizB = []
contador = 0
for i in range (4): #linhas
    for j in range (4): #colunas
        matrizB.append(int(input(f'Numero {i}x{j}: ')))
    matrizA.append(matrizB)
    matrizB = []
for i in matrizA: #cada lista dentro de matrizA
    for j in i: #cada valor dentro de i
        if j > 10:
            contador += 1
print(f'A quantidade e números maiores que 10 é, {contador}')
for i in range(len(matrizA)): #printar a matriz em forma de matriz
    print(matrizA[i]) #o valor de i vai ser cada linha printada

