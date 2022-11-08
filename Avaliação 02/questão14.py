#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
pessoas = int(input("Digite o total de pessoas: "))
soma = 0

for i in range(pessoas):
  idade = int(input("Digite aqui a sua idade: "))
  while idade < 0:
    print("Idade inválida, repita novamente.")
    idade = int(input("Digite aqui a sua idade: "))
  soma += idade
  media = soma / pessoas

if media > 0 and media <= 25:
  print("A média de idades é de uma turma jovem.")
else:
  if media > 25 and media <= 60:
    print("A média de idades é de uma turma adulta.")
  else:
    if media > 60:
      print("A média de idades é de uma turma idosa") 