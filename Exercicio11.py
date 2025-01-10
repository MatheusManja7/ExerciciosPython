def operacao(num1, num2, simbulo):
    if simbulo == "+":
        soma = num1 + num2
        print(f"Resposta: {soma}")

    elif simbulo == "-":
        if num1 > num2:
            subitracao1 = num1 - num2
            print(f"Resposta: {subitracao1}")

        else:
            subitracao2  = num2  - num1
            print(f"Resposta: {subitracao2}")

    if simbulo == "/":
        divisao = num1 / num2
        print(f"Resposta: {divisao}")

    if simbulo == "*":
        mult = num1 * num2
        print(f"Resposta: {mult}")               


print("")
num1 = float(input("Digite um Número: "))
num2 = float(input("Digite outro Número: "))
print("<------------------------->")
print("--Selecione a Opção Desejada--")
print("Selecione a Opção + para SOMA")
print("Selecione a Opção - para SUBITRAÇÃO")
print("Selecione a Opção / para DIVISÃO")
print("Selecione a Opção * para MULTIPLICAÇÃO")
simbulo = str(input("Operação desejada: "))    
print("<------------>")


res = operacao(num1,num2,simbulo)

print(res)