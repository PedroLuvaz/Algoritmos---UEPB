'Uma loja está vendendo seus produtos em 5 (cinco) prestações sem juros.'
'Faça um programa Python que receba um valor de uma compra e mostre o valor das prestações'

valor_produto = float(input('Qual foi o valor do produto ? '))
while valor_produto < 0:
    print('Por favor, insira um valor válido.')
    valor_produto = float(input('Qual foi o valor do produto ? '))
prestacao = valor_produto / 5
print(f"O valor do seu produto em 5x sem juros é de: {prestacao} R$")