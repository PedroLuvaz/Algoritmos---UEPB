#A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores, ou seja:
#Faça um programa em Python para mostrar os N primeiros termos da série de FETUCCINE, sabendo-se que para existir esta série serão necessários pelo menos três termos.
n1 = int(input("Digite aqui o valor para n1: "))
n2 = int(input("Digite aqui o valor para n2: "))
termos = int(input("Quantas repetições você quer ? "))
if termos < 3:
    print("Por favor, tente novamente, a quantidade minima de termos é 3.")
    exit()

n1 = n2
serie = 0

for i in range (3,termos):
    if(i%2==0):
        serie = n2 - n1
    else:
        serie = n2 + n1
    n1 = n2
    n2 = serie

    print(f"Os primeiros termos da série FETUCCINE são:{serie}")
