"Faça um Programa Python que converta metros para centímetros."
try:
   metros = float(input("Quantidade de metros que deseja converter em centímetros: "))
   while metros < 0:
      metros = float(input("Quantidade de metros que deseja converter em centímetros: "))
except ValueError:
   print("Valor inválido para comprimentos, digite apenas números > 0.")
   exit()
except KeyboardInterrupt:
   print("Programa finalizado, obrigado pelo uso.")
print(f"Resultado de {metros} metros para centímetros e de: {metros*100}")