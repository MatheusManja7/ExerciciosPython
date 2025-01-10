def ReversoDoNumero(numero):
    return int(str(numero)[::-1])


print()
numero = int(input("Digite Um Número: "))

reverso = ReversoDoNumero(numero)
print("<-------------------->")
print(f"O Reverso do Número {numero} é: {reverso}")