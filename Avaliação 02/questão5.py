#Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado.
quadrilateros = int(input("Insira a quantidade de quadriláteros que você quer calcular: "))
while quadrilateros < 0:
  quadrilateros = int(input("Insira a quantidade de quadriláteros que você quer calcular: "))  
for i in range(1,quadrilateros+1):
  lado = float(input("Digite aqui o valor para o lado: "))
  while lado < 0:
    lado = float(input("Digite aqui o valor para o lado: "))
  if lado < 0:
   print(f"Valor inválido para medidas, {lado}.")
  else:
    formula = lado**2 
    print(f"Resultado:{formula}")