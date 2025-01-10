def exclamacao(numero):
    for i in range(1, numero + 1):
        print("!" * i)

numero = int(input("Digite um Número: "))

linha_com_exclamacao = exclamacao(numero)

print(linha_com_exclamacao)