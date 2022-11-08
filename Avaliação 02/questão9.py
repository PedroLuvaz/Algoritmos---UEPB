#Fazer um programa que calcule e escreva a soma dos 50 primeiros termos da seguinte série:
valor = 1003
repeticao = 50
soma = 0

for i in range (1,repeticao+1):
  valor = valor - 3
  resultado = valor/i
  soma += resultado
  print(f"Resultado dos termos em sequência:{resultado}")
print(f"Resultado da soma dos primeiros 50 termos são:{soma}")