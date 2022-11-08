#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
numero1 = int(input("Insira aqui o número 1 do intervalo: "))
numero2 = int(input("Insira aqui o número 2 do intervalo: "))
while numero2 < numero1:
  print("Por favor insira o intervalo de maneira coerente [numero1 < numero2]") 
  numero1 = int(input("Insira aqui o número 1 do intervalo: "))
  numero2 = int(input("Insira aqui o número 2 do intervalo: "))

print("Os números correspondentes do seu intervalo são:")                                      
for i in range(numero1+1,numero2):
 
  print(i)