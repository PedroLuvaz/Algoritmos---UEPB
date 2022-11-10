#Escrever um programa Python para determinar o consumo médio de um automóvel.
#sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

try:
    distance = float(input('Digite aqui a distância percorrida: '))
    oil_consume = float(input('Digite aqui o consumo de gasolina: '))
except:
        print('Por favor, informe apenas valores corretos.')
        exit()
while distance < 0:
    print('Valor errado para distância, tente novamente.')
    distance = float(input('Digite aqui a distância percorrida: '))
while oil_consume <0:
    print('Valor errado para consumo, tente novamente')
    oil_consume = float(input('Digite aqui o consumo de gasolina: '))
distance_calculate = distance/oil_consume
print('A média de combustível gasto e a distância percorrida é de:',distance_calculate)

    

