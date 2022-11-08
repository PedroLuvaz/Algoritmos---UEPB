'Faça um programa Python que receba o preço de custo de um produto e mostre o valor de venda'
'Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário'

from curses.ascii import isalpha


valor_produto = float(input("Digite aqui o valor do produto: "))
while valor_produto < 0:
    print("Valor inválido, insira um valor correto para o produto.")
    valor_produto = float(input("Digite aqui o valor do produto: "))
acrescimo = float(input('Digite aqui o percentual de acréscimo do produto: '))
acrescimo_porcentagem = (acrescimo/100)
valor_finalproduto = (valor_produto * acrescimo_porcentagem) + valor_produto
print(f"O valor do produto com o acréscimo informado é de: {valor_finalproduto}")



