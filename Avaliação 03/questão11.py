'Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que'
'determine quantos alunos com mais de 13 anos possuem altura inferior à'
'média de altura desses alunos.'

idadeAlunos = []
alturaAlunos = []
media = 0

for i in range (5):
    print(f'aluno {i+1}')
    idadem = int(input(f'Digite aqui a idade do aluno {i+1}: '))
    alturam = float(input(f'Digite aqui a altura do aluno {i+1}: '))
    while idadem < 0 or alturam < 0:
        print('Valor inválido, tente novamente')
        idadem = int(input(f'Digite aqui a idade do aluno {i+1}: '))
        alturam = float(input(f'Digite aqui a altura do aluno {i+1}: '))      
    idadeAlunos.append(idadem)
    alturaAlunos.append(alturam)
    media += alturaAlunos[i]
    media_calculo = media/len(alturaAlunos)
    count13 = 0
for j in range (5):
    if idadeAlunos[j] >= 13 and alturaAlunos[j] < media:
        count13 += 1
print(idadeAlunos)
print([media_calculo])
print([count13])
    