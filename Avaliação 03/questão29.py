'Uma loja vende sapatos femininos de três marcas: A, B e C e tamanhos de 35 a'
'O gerente da loja lhe solicitou um programa para manipular dados referentes'
'ao estoque desta loja. Desta forma, você deve ler para cada marca de sapato e'
'numeração a sua respectiva quantidade e informar a numeração que possui a'
'maior quantidade em estoque. A seguir é apresentado um exemplo de tabela com'
'os dados do estoque.'
tamanhos = ['35','36','37','38','39','40']
listamarcas = []
listasoma = []
matrizMarcas = []
for marca in range(6):
    listamarcas.append([0]*3)

for i in range(6):
    for j in range (3):
        numeracao = 35
        quantidade = int(input(f'Digite aqui uma quantidade para a numeração {numeracao+i} da {j+1}ª Marca: '))
    
        listamarcas[i][j] = quantidade

print(listamarcas)

for i in range(len(listamarcas)):
        listasoma.append((sum(listamarcas[i])))

maiorvalor = max(listasoma)
maiorquantidade = listasoma.index(max(listasoma))
maior_tamanho = tamanhos[maiorquantidade]

#Calcular Matriz Transposta
for i in range(len(listamarcas[0])):
    matrizMarcas.append([0]*len(listamarcas))

for i in range(len(matrizMarcas)):
    for j in range(len(matrizMarcas[0])):
        matrizMarcas[i][j] = listamarcas[j][i]

for i in range(len(matrizMarcas)):
    print(matrizMarcas[i])

print(f"Numeração com maior quantidade em estoque: {maior_tamanho} ({maiorvalor} unidades)")



    
    











