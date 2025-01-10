###Exercício_4_Lista-EN-1###

print("-------------------CALCULADORA DE PAINÉIS SOLARES-------------------")
painelsolar_kwh = 40

def verificar_condicoes():
    while True:
        tamaho_tlhd = int(input("Digite o Tamanho do Seu Telhado (em metros quadrados):  "))
        if tamaho_tlhd < 10:
            print("Sua Residênsia não foi Aprovada para a Instalação de Paineis Solares")
            exit()
                
        orientacao_tlhd = str(input("Digite a Orientação do Seu Telhado:""\n""Digite n para - Norte""\n""s para - Sul""\n""Ou no para - Nenhuma Opção""\n""OP_:"))    
        if orientacao_tlhd == "no":
            print("Sua Residênsia não foi Aprovada para a Instalação de Paineis Solares")
            exit()


        sombreamento = str(input("Existe Algum Sombreamento Significante em sua Residência (árvores, prédios ou outros obstáculos): ""\n""Digite n para - Não""\n""s para - Sim" "\n" "OP_E"))
        if sombreamento != "n":
            print("Sua Residênsia não foi Aprovada para a Instalação de Paineis Solares")
            exit()
    
        return True

verificar_condicoes()

def quantidade_paineis():
    consumo_mmd_energia = int(input("Digite o Consumo Médio Mensal de Energia (Em KWh):  "))
    objetivo_reducao = int(input("Digite o objetivo de Redução ou Autossuficiência:  "))

    porcentagem = objetivo_reducao / 100
    cns_atendido_un = consumo_mmd_energia * porcentagem
    qntd_paineis = cns_atendido_un / painelsolar_kwh
    print(f"Sua Residência Necessitaráde {qntd_paineis} Painéis Solares")

quantidade_paineis()

        

    


                

