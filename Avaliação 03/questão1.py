'Faça um Programa que leia 5 números inteiros, armazene-os em uma lista.'

lista = []

for i in range(5):
    numero = int(input(f"Digite aqui o número {i+1} : "))
    lista.append(numero)
print(lista)