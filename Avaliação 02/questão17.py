#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo: Quantidade de Parcelas % de Juros sobre o valor inicial da dívida 1 0 3 10 6 15
#Exemplo de saída do programa: Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
#R 1.000,0001R  1.000,00 R 1.100,00103R  366,00 R 1.150,00156R  191,67
divida = float(input("Insira aqui o valor da divida: "))
if divida < 0:
    exit()
while divida > 0:
    parcela  = int(input("Digite aqui a quantidade de parcelas: "))
    if parcela < 0:
        print("Valor inválido para parcela, tente novamente.")
        exit()
    if parcela < 3:
        juros = 0
    else:
        if parcela == 3 or parcela <= 6:
            juros = (10/100)
        else:
            if parcela > 6:
                juros = (15/100)          
    valor_juros = divida * juros
    valor_parcela = (divida + valor_juros)/parcela
    print(f"Divida:{divida}")
    print(f"Juros:{valor_juros}")
    print(f"Quantidade de parcelas:{parcela}")
    print(f"Parcela:{valor_parcela}")
    divida = float(input("Insira aqui o valor da divida: "))

