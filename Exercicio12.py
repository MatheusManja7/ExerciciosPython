def somarnumeros(num1,num2):
    if num1 > num2:
        num1, num2 = num2, num1
    soma = 0
    for numero in range(num1,num2 + 1):
        soma += numero

    return soma

print()
numero1 = int(input("Digite um Número: "))        
numero2 = int(input("Digite outro Número: "))

res = somarnumeros(numero1,numero2)

print("<------------------------------------>")
print(f"O Resultado da Soma Entre os Números {numero1} e {numero2} é de: {res}")