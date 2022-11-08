#Escreva um programa que leia 10 números e informe o maior e o menor número.
Numero = float(input("Informe aqui o número: "))

maior = Numero
menor = Numero

for i in range(1,10):
  Numero = float(input("Digite aqui o valor de comparação: "))

  if Numero > maior:

    maior = Numero
  else:
    if Numero < menor:
      menor = Numero
print(f"o maior número é: {maior}, e o menor é: {menor}")