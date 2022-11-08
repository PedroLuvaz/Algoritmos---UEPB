sistemas = ['Windows Server','Unix','Linux','Netware','Mac Os','Outro']
votosistema = [0]*6
votos = -1
totalvotos = 0
i = 0
print('Qual é o melhor sistema operacional para uso em servidores ?')
print('='*100)
for k in range(len(sistemas)):
    print(k+1, '--->', '{}'.format(sistemas[k]))
    i += 1
print('='*100)
while votos != 0:
    votos = int(input('Digite aqui um valor entre 1 e 6 ou 0 para finalizar o programa: '))
    if not (0 < votos < 7):
        print('Digite aqui um valor entre 1 e 6 ou 0 para finalizar o programa: ')
        continue
    if votos == 0:
        print('Finalizando a apuração de votos.')
        break
    votosistema[votos - 1] += 1
    totalvotos += 1
print('O RESULTADO DA ENQUETE:')
print('='*100)
maiorvoto = 0
i = 0
for i in range(len(sistemas)):
    print('{} ---> {} ---> {:.2f}%'.format(sistemas[i],votosistema[i], votosistema[i]/float(totalvotos)*100))
    if votosistema[i] > votosistema[maiorvoto]:
        maiorvoto = i
    i += 1
print('='*100)
print('Total de votos: {}'.format(totalvotos))
print('='*100)
print('O vencedor da enquete foi o sistema {}, com {} votos, correspondendo ao percentual de {:.2f}% ''dos votos válidos'.format(sistemas[maiorvoto], votosistema[maiorvoto],(votosistema[maiorvoto])/float(totalvotos)*100))


