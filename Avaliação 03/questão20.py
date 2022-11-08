'Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma'
'busca desse valor na matriz e, ao ﬁnal, escrever a localizacão (linha e coluna)'
'ou uma mensagem de “não encontrado”.'
'na diagonal principal.'
Matriz = []
MatrizB = []
for l in range (3): #linhas
    for c in range (3): #colunas
        Matrizvalor = int(input(f'Digite aqui o número {l}x{c}: '))
        MatrizB.append(Matrizvalor)
        Matriz.append(MatrizB)
    MatrizB = []

procura = int(input('Digite aqui um valor:  '))
achou = False
i = 0
while not achou and i < len(MatrizB):
  j = 0
  for j in range(len(MatrizB)):
      if procura == Matriz[i][j]:
        print(f'Encontrado em: {i+1}X{j+1}')
        achou = True
      else:
        j+=1
  i += 1

if not achou:
    print("Não encontrado")





    





