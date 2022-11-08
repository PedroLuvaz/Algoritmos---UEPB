'Faça um Programa que leia uma lista A com 10 números inteiros, calcule e'
'mostre a soma dos quadrados dos elementos do vetor.'

lista = []
quadrado = 1
soma = 0
lista_final = []

for i in range (10):
    numero = int(input(f'Digite aqui o número {i+1}: '))
    quadrado = numero ** numero
    soma += quadrado
    lista.append(numero)
    lista_final.append(soma)
print(f'Os números informados: {lista}')
print(f'A soma dos quadrados dos elementos = {soma}')
