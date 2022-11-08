'Faça um Programa que leia 40 notas, mostre as notas e a média na tela.'
listaNotas = []
media = 0
print ('Informe as 40 notas')
for notas in range(40):
    listaNotas.append(float(input(f'Nota {notas+1}: ')))
    media += listaNotas[notas]
    calculo_media = media/40
print(f'lista com as notas: {listaNotas}') 
print(f'media: {calculo_media}')