#Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
soma = 0
denominador = -1
numerador = int(input("Digite aqui o número de expressões que quer (não coloque valores < 0): "))
while numerador < 0:
  numerador = int(input("Digite aqui o número de expressões que quer (não coloque valores < 0):"))

for i in range (1,numerador+1):
  denominador += 2
  operacao = i/denominador
  soma += operacao
  print(f"Todas as expressões a seguir:{soma}")