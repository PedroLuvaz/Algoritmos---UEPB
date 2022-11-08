#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero = int(input("Informe aqui um número para verificar se ele é primo: "))
while numero < 0:
  numero = int(input("Informe aqui um número para verificar se ele é primo: "))
cont = 0

for i in range(numero):
  if numero%(i+1) == 0:
     cont += 1
  else:   
     cont

if cont == 2:
  print("Esse número é primo.")

else:
  print("Esse número não é primo.")