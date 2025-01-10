def convercao(celcios):
    fahrenheit = celcios * (9/5) + 32
    return fahrenheit

print()
print("--Converção de Graus Celcios em Fahrenheit--")
celcios = int(input("Digite um um Valor correspondente aos Graus Celcios: "))    

res = convercao(celcios)
print("<---------------------------------------------->")
print(f"{celcios} Graus Celcis é Equivalente a {res} Fahrenheit")