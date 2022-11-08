'Faça um Programa que leia duas listas com 10 elementos cada. Gere uma'
'terceira lista de 20 elementos, cujos valores deverão ser compostos pelos'
'elementos intercalados das duas outras listas'

lista1 = []
lista2 = []
lista3 = []

for one in range(10):
    lista1.append(input("Digite aqui os elementos para a lista 1: "))
for two in range(10):
    lista2.append(input("Digite aqui os elementos para lista 2: "))
for tree in range(10):
    lista3.append(lista1[tree])
    lista3.append(lista2[tree])
print(f'Elementos da lista1: {lista1}')
print(f'Elementos da lista2: {lista2}')
print(f'A composição da lista3: {lista3}')