#Questão 13

listaTemperaturas = []
listaMeses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

print('''Meses Do Ano:

1-Janeiro
2-Fevereiro
3-Março
4-Abril
5-Maio
6-Junho
7-Julho
8-Agosto
9-Setembro
10-Outubro
11-Novembro
12-Dezembro
''')

for i in range(1, 13):

    try:
        temperaturaMes = float(input(f"Informe a temperatura média para o {i}º Mês:"))
    except ValueError:
        print("ERRO: A Temperatura Deve Ser Um Valor Numérico!")
        exit()
    except KeyboardInterrupt:
        print("\nPrograma Finaliado!")
        exit()

    listaTemperaturas.append(temperaturaMes)

somaTemperaturas = sum(listaTemperaturas)
mediaTemperatura = (somaTemperaturas / 12)

print("-" * 50)
print(f"Média Anual: {mediaTemperatura} ºC")
print("-" * 50)

for compararMedia in range(12):
    if (listaTemperaturas[compararMedia] > mediaTemperatura):
        print(f"{listaMeses[compararMedia]} = {listaTemperaturas[compararMedia]} ºC")