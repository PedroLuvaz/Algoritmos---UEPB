'Faça um Programa Python que peça 2 números inteiros e um número real.'
'Calcule e mostre: a. o produto do dobro do primeiro com metade do segundo'
'b. a soma do triplo do primeiro com o terceiro.'
'c. o terceiro elevado ao cubo.'
def pularlinha():
    print('='*50)


try:
    num_a = int(input('Digite aqui o valor para A: '))
    num_b = int(input('Digite aqui o valor para B: '))
    num_c = float(input('Digite aqui o valor para C: '))
except ValueError:
    print('Obrigado por utilizar o programa.')
    exit()

operation_a = (num_a * 2) + (num_b / 2)
operation_b = (num_a * 3) + num_c
operation_c = (num_c ** 3)

pularlinha()
print(f'O produto do dobro do primeiro com metade do segundo é:\n{operation_a}')
pularlinha()
print(f'A soma do triplo do primeiro com o terceiro é:\n{operation_b}')
pularlinha()
print(f'O terceiro elevado ao cubo é:\n{operation_c}')
pularlinha()