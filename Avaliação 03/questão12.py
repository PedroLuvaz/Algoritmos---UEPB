'Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e'
'armazene os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a'
'leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem'
'ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados'
'na lista), ou NÃO ACHEI caso contrário.'

nomes = []

for i in range (10):
    nomes_lista= input(f"Adicione um nome, nome {i+1}: ")
    nomes.append(nomes_lista)
    count = 1
while (count < 4):
     adivinha = input('Digite aqui um nome para consultar na lista: ')

     if adivinha in nomes:
        print('Achei!')
     else:
        print('Não achei')
        count += 1
