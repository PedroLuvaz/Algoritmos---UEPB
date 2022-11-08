'4. Faça um Programa que leia 20 números inteiros e armazene-os numa lista.'
'Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.'

listatotal = []
listapar = []
listaimpar = []

for i in range (10):
    numero = int(input("Digite aqui um número: "))
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    listatotal = listapar+listaimpar
    listatotal.sort()
print(f'Os numeros pares: {listapar}')
print(f'Os numeros impares: {listaimpar}')
print(f'Todos os numeros informados: {listatotal}')



