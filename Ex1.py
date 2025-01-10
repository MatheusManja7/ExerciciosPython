###Exercício_1_Lista-EN-1###
print("-----------------------------CALCULADORA-----------------------------")
n1 = float(input("Digite o Numero Desejado: "))
operador = input("Escolha o o Operador que você deseja:" "\n" "Soma ---> +" "\n" "Subitração ---> -" "\n" "Multiplicação ---> *" "\n" "Divisão ---> /" "\n" "--->") 

if operador == "+":
    n2 = float(input("Digite outro numero: "))
    soma = (n1 + n2)
    print(soma)

elif operador == "-":
    n2 = float(input("Digite outro numero: "))
    subitração = (n1 - n2)
    print(subitração)

elif operador == "*":
    n2 = float(input("Digite outro numero: "))
    multiplicação = (n1 * n2)
    print(multiplicação)

elif operador == "/":
    n2 = float(input("Digite outro numero: "))
    divisão = (n1 / n2)
    print(divisão)

else:
    print("ERRO!!!")    

