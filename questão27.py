"""27. Faça um programa que leia duas matrizes 2 x 2 com valores reais. Ofereça ao
usuário um menu de opções: (a) somar as duas matrizes (b) subtrair a primeira
matriz da segunda (c) adicionar uma constante `as duas matrizes (d) imprimir
as matrizes. Nas duas primeiras opções uma terceira matriz deve ser criada.
Na terceira opção o valor da constante deve ser lido e o resultado da adição da
constante deve ser armazenado na própria matriz."""

matriz1 = []
matriz2 = []
resposta = ""

for i in range(1, 3):
    linha = []
    for k in range(1, 3):
        valor = input("Digite um valor: ")
        while valor.isalpha():
            valor = input("Inválido! Digite um valor numérico: ")
        valor = int(valor)
        linha.append(valor)
    matriz1.append(linha)

for i in range(1, 3):
    linha = []
    for k in range(1, 3):
        valor = input("Digite um valor: ")
        while valor.isalpha():
            valor = input("Inválido! Digite um valor numérico: ")
        valor = int(valor)
        linha.append(valor)
    matriz2.append(linha)

while resposta in "ABCD":

    resposta = input(
        "Opções: \nA)Somar matrizes\nB)Subtrair matrizes\nC)Adicionar constante\nD)Imprimir matrizes").upper()

    if resposta == "A":
        matrizSomada = []
        for x in range(0, 2):
            linha = []
            for y in range(0, 2):
                valor = matriz1[x][y] + matriz2[x][y]
                linha.append(valor)
            matrizSomada.append(linha)
        for i in matrizSomada:
            print(i)

    elif resposta == "B":
        matrizSubtraida = []
        for x in range(0, 2):
            linha = []
            for y in range(0, 2):
                valor = matriz1[x][y] - matriz2[x][y]
                linha.append(valor)
            matrizSubtraida.append(linha)
        for i in matrizSubtraida:
            print(i)

    elif resposta == "C":
        constante = input("Digite uma constante a ser aplicada: ")
        while constante.isalpha():
            constante = input("Inválido! Digite uma constante a ser aplicada: ")
        constante = int(constante)

        for x in range(0, 2):
            for y in range(0, 2):
                valor = matriz1[x][y] + constante
                matriz1[x][y] = valor

        for x in range(0, 2):
            for y in range(0, 2):
                valor = matriz2[x][y] + constante
                matriz2[x][y] = valor
    elif resposta == "D":
        print("---Matriz 1---")
        for i in matriz1:
            print(i)
        print("---Matriz 2---")
        for i in matriz2:
            print(i)

