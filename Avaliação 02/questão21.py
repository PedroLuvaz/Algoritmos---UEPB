#O cardápio de uma lanchonete é o seguinte: Especificação Código Preço Cachorro Quente 100 R 1,20BauruSimples101R  1,30 Bauru com ovo 102 R 1,50Hambúrguer103R  1,20 Cheeseburguer 104 R 1,30Refrigerante105R  1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
Cachorro_quente = 100      #preço 1,20
Bauru_Simples = 101        #preço 1,30
Bauru_com_Ovo = 102        #preço 1,50
Hamburguer = 103           #preço 1,20
Cheeseburguer = 104        #preço 1,30
Refrigerante = 105         #preço 1,00
valor = 0
quantidade = 0
valor_final = 0
conta = 0
lanches = 0

pedido = int(input("Qual o seu pedido (digite 0 para parar o seu pedido.) ? "))
if pedido == 0:
    print("Obrigado pela preferência, encerrando atendimento.")
    exit()
else:
    if pedido < 99 or pedido > 105:
        print("Valor de código inválido, tente novamente.")
        exit()
    else:    
        quantidade = int(input("Quantidade: "))
while pedido >= 100 and pedido < 106:
    if pedido == 101 or pedido == 104:
        valor = 1.30
        valor_final = valor * quantidade
    else:
        if pedido == 100 or pedido == 103:
            valor = 1.20
            valor_final = valor * quantidade
        else:
            if pedido == 102:
                valor = 1.50
                valor_final = valor * quantidade
            else:
                valor = 1.00
                valor_final = valor * quantidade
    lanches += quantidade
    conta += valor_final
    print(f"O seu pedido teve um valor de:{conta}")
    print(f"Foram feitos um total de: {lanches} lanches")
    pedido = int(input("Qual o seu pedido (digite 0 para parar o seu pedido.) ? "))
    if pedido == 0:
        print("Obrigado pela preferência, encerrando atendimento.")
        exit()
    else:
        if pedido < 99 or pedido > 105:
            print("Valor de código inválido, tente novamente.")
            exit()
        else:    
            quantidade = int(input("Quantidade: "))
