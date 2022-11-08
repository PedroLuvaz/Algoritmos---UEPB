'Faça um programa que leia um número indeterminado de valores,'
'correspondentes a notas, encerrando a entrada de dados quando for informado'

'um valor igual a -1 (que não deve ser armazenado). Após esta entrada de'
'dados, faça:'
'a. Mostre a quantidade de valores que foram lidos;'
'b. Exiba todos os valores na ordem em que foram informados'
'c. Exiba todos os valores na ordem inversa à que foram informados'
'd. Calcule e mostre a soma dos valores;'
'e. Calcule e mostre a média dos valores;'
'f. Calcule e mostre a quantidade de valores acima da média calculada;'
'g. Calcule e mostre a quantidade de valores abaixo de sete;'
'h. Encerre o programa com uma mensagem.'
notas = []
reversa = []
soma = 0
val = 0
countacima = 0
countbaixo = 0
while val != -1:  
    val = int(input('Digite o valor: '))
    if val == -1:
      print('Parando a contagem.')
    else:
      notas.append(val)
      reversa.append(val)
      soma += val
      media = soma/len(notas)
    if val > media:
        countacima += 1
    if val < 7:
        countbaixo += 1
countbaixo = countbaixo - 1
reversa.reverse()
print(f'A quantidade de números da lista: {len(notas)}')
print(f'A lista na ordem citada: {notas}')
print(f'A lista em ordem reversa: {reversa}')
print(f'A soma dos números da ordem: {soma}')
print(f'A media dos números citados: {media}')
print(f'A quantidade de valores acima da média é de: {countacima}')
print(f'A quantidade de valores menores que 7 são: {countbaixo}')
print('Finalizando o programa...')

