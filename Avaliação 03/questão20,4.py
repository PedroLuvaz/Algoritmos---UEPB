matriz = []
for i in range(5): 
    linha = [] 
    for j in range(5):
      linha.append(int(input('Digite o valor [' + str(i+1) + ',' + str(j+1) + ']:' )))
    matriz.append(linha)
valor = int(input('Informe o valor para encontrar: '))

achou = False

i = 0

while not achou and i < len(matriz):
  j = 0
  for j in range(len(matriz)):
      if valor == matriz[i][j]:
        print(f'Encontrado em: {i+1}X{j+1}')
        achou = True
      else:
        j+=1
  i += 1

if not achou:
    print("Não encontrado")