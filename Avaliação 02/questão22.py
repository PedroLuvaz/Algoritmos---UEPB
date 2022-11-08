#Você foi contratado para escrever um algoritmo que calcule quantos pontos fez um time num campeonato de futebol. Para os que não conhecem futebol uma vitória vale três pontos, um empate vale 1 ponto e a derrota não vale ponto. A entrada será composta por pares de números indicando o resultado de cada jogo. O primeiro número sempre corresponde ao total de gols que o time fez no jogo. A leitura dos dados será finalizada quando for fornecido um número de gols negativo

time_1 = time_2 = pontos = 0

while time_1 >= 0 and time_2 >= 0:
    if time_1 < 0 or time_2 < 0:
        exit()
  
    time_1 = int(input("Gols do 1º time: "))
    time1 = int(time_1)

    time_2 = int(input("Gols do time adversário: "))
    time_2 = int(time_2)

    if time_1 == time_2:
        pontos += 1
    elif time_1 < time_2:
        pontos += 0
    else:
        pontos += 2

    print(f"Pontuação: {pontos}")