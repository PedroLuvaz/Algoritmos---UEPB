#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber: a) Média do salário da população; b) Média do número de filhos; c) Maior salário; d) Percentual de pessoas com salário até R$250,00. Desenvolver um programa para calcular e escrever o que foi pedido nos itens a, b, c e d. O final da leitura de dados se dará com a entrada de um salário negativo.
salario = 0
soma_salario = 0
soma_num_filhos = 0
num_participantes = 0
salario_ate_250 = 0
maior_numero = 0

while salario >= 0: #enquanto o salario for maior que zero continuar rodando
    salario = float(input('Qual o seu salário? '))
    if salario >= 0:
        num_filhos = int(input('Qual o número de filhos? '))
        while num_filhos < 0:
            print('Valor inválido! Tente novamente')
            num_filhos = int(input('Qual o número de filhos? '))
        soma_salario += salario #soma salário somará cada salário digitado
        soma_num_filhos += num_filhos #soma_num_filhos somará o número de filhos de cada participante
        num_participantes += 1 #contador que sempre vai adicionar 1 se o participante escrever um salário >=0
        if salario > maior_numero:
            maior_numero = salario #atualiza o número de maior salário
        if salario <= 250:
            salario_ate_250 +=1 #contador: números de pessoas que tem salário até 250

    else: #caso o salario for menor que zero, fazer calculos, mostrar resultados e encerrar programa
        print('Valor inválido! Encerrando programa e mostrando resultados...')
        media_salario = soma_salario/num_participantes
        media_filhos = int(soma_num_filhos/num_participantes)
        porcent_salario_ate_250 = (salario_ate_250 / num_participantes) * 100
        print(f'Média do salário da população: {media_salario:.2f}$')
        print(f'Média dos filhos da população: {media_filhos}')
        print(f'Maior salário: {maior_numero:.2f}$')
        print(f'Percentual de pessoas com salário até R$250,00: {porcent_salario_ate_250}%')