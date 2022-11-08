#Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faça um programa para gerar e mostrar o número H. O número N será fornecido como entrada.
denominador = int(input("Insira aqui o valor para o denominador: "))
H = 0

for i in range(denominador):                 # 1 + 1/2 + 1/3 + 1/4
  formula = 1 / (i+1)   
  H += formula
print(f"Resultado: {H}")