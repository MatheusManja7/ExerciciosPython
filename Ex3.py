###Exercício_3_Lista-EN-1###
porcentagem = 0.10
cardapio = str(input(" Deseja ver O Cardápio? (sim) ou (não): "))
               
while cardapio == "sim":
    print("1 ---> Lasanha de Frango - R$ 45,00 ")
    print("2 ---> Salmão Grelhado com Legumes - R$ 50,00 ")
    print("3 ---> Risoto de Cogumelos - R$ 40,00 ")
    print("4 ---> Frango à Parmegiana - R$ 42,00 ")
    print("5 ---> Espaguete à Bolonhesa - R$ 38,00 ")
    print("6 ---> Feijoada Completa - R$ 50,00 ")
    print("7 ---> Pudim de Leite Condensado - R$ 15,00 ")
    print("8 ---> Torta de Limão - R$ 18,00 ")


    prato_escolhido = float(input("Para Realizar seu Pedido Digite o Número do Prato Escolhido: "))
    qntd = int(input("Digite a Quantidade Desejada: "))

    match cardapio:
        case 1:
            valor_do_prato = 45.00
            valor_do_pedido = valor_do_prato * qntd

        case 2:
            valor_do_prato = 50.00
            valor_do_pedido = valor_do_prato * qntd

        case 3:
            valor_do_prato = 40.00
            valor_do_pedido = valor_do_prato * qntd        

        case 4:
            valor_do_prato = 42.00
            valor_do_pedido = valor_do_prato * qntd

        case 5:
            valor_do_prato = 38.00
            valor_do_pedido = valor_do_prato * qntd

        case 6:
            valor_do_prato = 50.00
            valor_do_pedido = valor_do_prato * qntd

        case 7:
            valor_do_prato = 15.00
            valor_do_pedido = valor_do_prato * qntd

        case 8:
            valor_do_prato = 18.00
            valor_do_pedido = valor_do_prato * qntd  

    pagamento_total = valor_do_pedido

    mais_pedidos = str(input("Você Deseja Realizar Mais Pedidos?" "\n" "sim" "não"))      

gorjeta = str(input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato: "))
if gorjeta == "sim":
    adicional = pagamento_total * porcentagem
    pagamento_final = valor_do_pedido + adicional
    print("Seu Pedido Ficou em Um Total de:",pagamento_final)

else:
    print("Seu Pedido Ficou em Um Total de:",pagamento_total)

