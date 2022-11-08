#Escreva um programa que calcula o fatorial de um dado número N.

numero = int(input("Fatorial de: ") )         #exemplo
                                              #resultado = 1 * 1
resultado=1                                   #resultado = 2 * 1
for n in range(1,numero+1):                   #resultado = 3 * 2
    resultado = n * resultado                 #resultado = 4 * 6
                                              #resultado = 5 * 24
print(resultado)