#Escreva um programa Python que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão
# D = R+2sobre2, onde R (A + B)^2 e S (B + C)^2
#A = 0 B = 1 C = 2 NO LAÇO FOR
var = ['A','B','C']
values = []
for i in range (3):
    try:
        number = int(input(f'Digite aqui o valor {var[i]}: '))
        if number > 0:
            values.append(number)
    except:
        print('Por favor, não digite apenas simbolos ou letras.')
        exit()
    while number.isnumeric() < 0:
        print('Por favor, insira apenas valores corretos.')
        number = int(input(f'Digite aqui o valor {var[i]}: '))
        if number >0:
            values.append(number)
R = (values[0] + values[1])**2
S = (values[1] + values[2])**2
D = (R + S)/2
print(var)
print(f'Os valores associados às variáveis: {values}')
print(f'O valor da expressão é: {D}')


    