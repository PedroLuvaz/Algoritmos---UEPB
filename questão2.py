'Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.'

lista = []

for i in range (4):
    numero = float(input(f"Digite aqui o número {i+1}: "))
    lista.append(numero)
lista.reverse()
print(lista)

