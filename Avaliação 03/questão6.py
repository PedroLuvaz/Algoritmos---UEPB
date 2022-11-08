'Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a multiplicação e os numeros.'
numeros_lista = []
somas_lista = []
multiplicacao_lista = []
soma = 0
multiplicacao = 1

for i in range (5):
    numeros= int(input(f"Digite aqui o número {i+1}: "))
    soma += numeros
    somas_lista.append(soma)
    multiplicacao *= numeros
    multiplicacao_lista.append(multiplicacao)
    numeros_lista.append(numeros)

print(f'Os numeros que foram ditos: {numeros_lista}')
print(f'O resultado da soma dos números: {[somas_lista[-1]]}')
print(f'O resultado da multiplicação dos números: {[multiplicacao_lista[-1]]}')
