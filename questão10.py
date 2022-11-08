'Altere o programa anterior, intercalando 3 listas de 10 elementos cada'

lista1 = []
lista2 = []
lista3 = []
lista4 = []

for one in range(3):
    lista1.append(input("Digite aqui os elementos para a lista 1: "))
for two in range(3):
    lista2.append(input("Digite aqui os elementos para lista 2: "))
for tree in range(3):
    lista3.append(input("Digite aqui os elementos para a lista3: "))
for four in range(3):
    lista4.append(lista1[four])
    lista4.append(lista2[four])
    lista4.append(lista3[four])
print(f'Elementos da lista1: {lista1}')
print(f'Elementos da lista2: {lista2}')
print(f'Elementos da lista3: {lista3}')
print(f'A composição da lista4: {lista4}')