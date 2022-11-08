#Faça um programa para calcular um valor A elevado a um expoente B. Os valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de repetição.
valor_a = float(input("Insira aqui um valor para a: "))
valor_b = int(input("Insira aqui um valor para b: "))
resultado = valor_a

while valor_b < 0:
  valor_b = int(input("Insira aqui um valor para b: "))          

if valor_b == 0:
  resultado = 1

for i in range(1,valor_b): 
  resultado *= valor_a

print(f"Resultado: {resultado}") 