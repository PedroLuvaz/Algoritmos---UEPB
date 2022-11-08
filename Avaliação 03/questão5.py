'Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene'
'numa lista a média de cada aluno, imprima o número de alunos com média'
'maior ou igual a 7.0.'
mediasalunos = []
notasaluno = []
aprovados = 0

for i in range (10):
  media = 0
  notasaluno = []
  print(f'Aluno {i+1}')
  for j in range (4):
          nota_aluno = float(input(f'Digite aqui a nota {j+1}: '))
          while nota_aluno < 0 or nota_aluno > 10:
            nota_aluno = float(input(f'Digite aqui a nota {j+1}: '))
          notasaluno.append(nota_aluno)
          media += notasaluno[j]
  media_final = media/4
  if media_final >= 7:
     aprovados +=1
  mediasalunos.append(media_final)
print(f'A lista das médias dos alunos em ordem: {mediasalunos}')
print(f'A quantidade de alunos com a média maior ou igual a 7: {aprovados}')
