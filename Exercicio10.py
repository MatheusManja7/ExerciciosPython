def calcular_media(nota1, nota2, nota3, letra):
    if letra == "a":
        media_aritimetica = (nota1 + nota2 + nota3) / 3
        print("<---------------------------->")
        print(f"Sua Média Aritimética é {media_aritimetica}")

    elif letra == "b":
        calculo1 = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
        media_ponderada = calculo1 / (peso1 + peso2 + peso3)
        print("<---------------------------->")
        print(f"Sua Média Ponderada é {media_ponderada}") 

#pesos
peso1 = 5
peso2 = 3
peso3 = 2

print()
print("--Calcular Média--")
#notas e letra
nota1 = int(input("Digite o a Primeira Nota: "))    
nota2 = int(input("Digite o a Segunda Nota: "))    
nota3 = int(input("Digite o a terceira Nota: "))
letra = str(input("Digite A para - Média Aritimetica ou B para - Média Ponderada: "))

res = calcular_media(nota1,nota2,nota3,letra)



