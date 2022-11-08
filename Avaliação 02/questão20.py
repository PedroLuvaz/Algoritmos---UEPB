#Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.
numero = int(input("Digite aqui um número: "))
countnumeros = 0
numero_par = 0
media_par = 0
soma = 0
numero_impar = 0
media_impar = 0
media_geral = 0
while numero > 0:
  countnumeros += 1
  soma += numero
  media_geral = soma / countnumeros
  if numero % 2 == 0:
    numero_par += 1
    media_par = numero_par / countnumeros
  else:
    numero_impar += 1
    media_impar = numero_impar / countnumeros
    soma += numero

  print(f"A quantidade números pares é de:{numero_par}")
  print(f"A quantidade de números impares é de:{numero_impar}")
  print(f"A média geral dos números pares é de:{media_par}")
  print(f"Foram lidos um total de {countnumeros} numeros")
  print(f"A média geral dos números lidos foi de: {media_geral}")
  numero = int(input("Digite aqui um número: "))