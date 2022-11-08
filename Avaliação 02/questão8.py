#Faça um programa para: a) Ler um valor x qualquer b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+…(x+100).
valor_x = int(input("Insira aqui o valor para x: "))
soma = 0

for i in range(1,100+1):
  y = (valor_x+i)
  resultado = y
  soma+=resultado
print(f"Resultado:{soma}")