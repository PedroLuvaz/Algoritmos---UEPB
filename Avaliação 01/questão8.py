#Escrever um programa Python que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas

def positivo(numero):
    while numero <= 0:
        numero = float(input(f'Informe apenas valores positivos: '))
    return numero

def quebralinha():
    print('='*50)

name = input('Digite aqui o seu nome: ')
wage = float(input('Digite aqui o seu salário: '))
wage = positivo(wage)
sales = int(input('Digite o número de vendas: '))
sales = positivo(sales)
salesprices = float(input('Digite aqui o valor total das vendas que foram realizadas: '))
salesprices = positivo(salesprices)
bonus = ((15/100) * (salesprices)) + wage

quebralinha()
print(f'Nome do colaborador = {name}')
quebralinha()
print(f'Salário normal = {wage}')
quebralinha()
print(f'Numero de vendas = {sales}')
quebralinha()
print(f'O salário do colaborador com o bônus de vendas é de: {bonus}')
quebralinha()










