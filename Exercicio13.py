def exponenciacao(x, z):
    operacao = x ** z
    return operacao



x = int(input("Digite um Número referente a Base: "))   
z = int(input("Digite um Número referente a Expoente: "))

res = exponenciacao(x,z)

print(res)