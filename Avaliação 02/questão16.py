#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
#programa que leia um conjunto indeterminado de temperaturas, e informe ao
#final a menor e a maior temperatura informada, bem como a média das
#temperaturas.

resposta = "S"

maior_temperatura = menor_temperatura = 0

soma_total = 0
contador = 0

while resposta == "S":
    
    resposta = input("Adicionar novos dados[S/N]: ").upper()
    
    while resposta not in "SN":
            resposta = input("Adicionar novos dados[S/N]: ").upper()

    if resposta == "S":
        temperatura = input("Temperatura °C: ")
        
        while temperatura.isalpha():
            temperatura = input("Inválido, temperatura °C: ")
        temperatura = float(temperatura)

        soma_total += temperatura
        contador += 1

        if contador == 1:
            maior_temperatura = menor_temperatura = temperatura
        
        if temperatura < menor_temperatura:
            menor_temperatura = temperatura

        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
    
    elif resposta == "N":
        print(f"Maior temperatura registrada: {maior_temperatura} Menor temperatura: {menor_temperatura} Média de temperatura: {soma_total/contador}")