'16. Escreva um programa em Python para encontrar o segundo maior elemento de'
'uma lista com 20 números inteiros.'
'OBS: todos os valores informados serão de valores diferentes e a solução não'
'deve fazer este tratamento das entradas. Além disso, a solução não deve'
'modificar a lista original com a ordem fornecida dos números.'
numeros_lista = []

for i in range (4):
    numeros = int(input(f'Digite aqui o número {i+1}: '))
    while numeros in numeros_lista:
        print('Por favor, não coloque números repetidos.')
        numeros = int(input(f'Digite aqui o número {i+1}: '))
    numeros_lista.append(numeros)
print(f'A sua lista é: {numeros_lista}\nE o segundo maior número é: {sorted(numeros_lista)[-2]}')
