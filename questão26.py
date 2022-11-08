"""26. Escreva um programa que transforme uma matriz 4x4 numa matriz triangular
inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal
principal. Imprima a matriz original e a matriz transformada."""

matriz = []

for l in range(4):
    linha = []
    for c in range(4):
        valor = input(f"Digite o valor para {l}x{c}: ")
        while valor.isalpha():
            valor = input("Inválido! Digite um valor numérico: ")
        valor = int(valor)
        linha.append(valor)
    matriz.append(linha)

print("---Matriz Normal---")

for i in matriz:
    print(i)

for l in range(4):
    for c in range(4):
        if c > l:
            matriz[l][c] = 0

print("---Matriz Triangular---")

for j in matriz:
    print(j)
