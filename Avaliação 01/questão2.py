"Faça um Programa Python que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês."
"Calcule e mostre o total do seu salário no referido mês."

try:
    valor = float(input("Quanto você recebe por hora ? "))
    trab = float(input("Quantas horas você trabalhou esse mês ? "))
    while valor < 0:
        valor = float(input("Quanto você recebe por hora ?"))
    while trab < 0:
        trab = float(input("Quantas horas você trabalho esse mês ?"))
except ValueError:
    print("Por favor, digite apenas números.")
    exit()
print(f'O seu salário é de: {valor*trab}')
