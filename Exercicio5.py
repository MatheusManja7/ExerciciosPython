def maiornumero(num1,num2,num3):
    return max(num1,num2,num3)
    

print()
num1 = float(input("Digite um Número: "))    
num2 = float(input("Digite Outro Número: "))    
num3 = float(input("Digite Mais um Número: "))    

maior_numero = maiornumero(num1,num2,num3)

print("<---------------------------------------->")
print(f"O Maior Número entre {num1}, {num2} e {num3} é: {maior_numero}")