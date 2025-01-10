import random

numeros = []

def sorteia(inicio, fim, quantidade):
    global numeros
    numeros = [random.randint(inicio, fim) for _ in range(quantidade)] 
   
inicio = 1
fim = 100
quantidade = 5



def somaPar(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)

    soma = sum(pares)
    print("<------------------------------------->")
    print(f"Números Sorteados: {numeros}")
    print(f"A Soma dos Números Pares Sorteados são: {soma}")     

res1 = sorteia(inicio,fim,quantidade)
res2 = somaPar(numeros)


