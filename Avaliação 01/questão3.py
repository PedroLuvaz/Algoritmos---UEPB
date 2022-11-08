"Faça um Programa Python que peça a temperatura em graus Farenheit,"
"transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)."

try:
    far = float(input("Qual é a temperatura em Farenheit que deseja converter para Celsius ? "))
    conversao = (5*(far-32)/9)
except KeyboardInterrupt:
    print("Encerrando o programa.")
print(f'A temperatura {far}em Farenheit para Celsius é de:{conversao}')


