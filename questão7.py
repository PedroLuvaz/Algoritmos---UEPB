'Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada'
'informação na sua respectiva lista. Imprima a idade da pessoa que possui maior altura'

idade = []
altura = []
for i in range (10):
        print(f'Pessoa {i+1}')
        idadem = int(input('Digite aqui a sua idade: '))
        alturam = float(input('Digite aqui a sua altura: '))
        while idadem < 0 or alturam < 0:
            print('Valor inválido, tente novamente.')
            idadem = int(input('Digite aqui a sua idade: '))
            alturam = float(input('Digite aqui a sua altura: '))
        altura.append(alturam)
        idade.append(idadem)
        max(altura)
        indexAltura =  altura.index(max(altura))
print(f'A idade da pessoa com a maior altura é:{[idade[indexAltura]]}')