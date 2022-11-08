#Escreva um programa que calcula a média de 30 alunos e informa a situação (reprovado, aprovado ou recuperação).
alunos = 5
for i in range(1,alunos+1):
  nota = float(input("Digite aqui a nota 1: "))
  nota2 = float(input("Digite aqui a nota 2: "))
  media = (nota + nota2)/2
  if nota < 0 or nota2 < 0 or nota > 10 or nota2 > 10:
     print("Valor inválido para nota.")
  else:
    if media >= 7:
       print("Aprovado!")
       print(f"Media: {media}, aluno: {i}")
    else:
       if nota >= 4 and nota < 7:
          print(f"Recuperação: {media}, aluno: {i}")
       else:
          print(f"Reprovado: {media}, aluno: {i}")