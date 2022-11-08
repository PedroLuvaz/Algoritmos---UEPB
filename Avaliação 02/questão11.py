contadorO = 0
contadorB = 0 
contadorR = 0
idademedia = 0
for i in range(5):
  idade = int(input('Qual sua idade: '))
  opiniao = int(input('Qual sua opinião: 3-ótimo 2-bom 1-regular: '))
  if opiniao == 3:
    contadorO += 1
    idademedia += idade
    idade += idade   
    media = idademedia/contadorO
  elif opiniao == 1:
    contadorR +=1
  elif opiniao == 2:
    contadorB += 1
    porcentagem = contadorB*(15/100)
  
print(f'A media de idade de quem disse otimo foi: {media}')
print(f'Quantidade de pessoas que responderam regular: {contadorR}')
print(f'A porcentagem de pessoas que responderam bom: {porcentagem}%')