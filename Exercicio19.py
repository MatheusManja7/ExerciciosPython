def triangulo(linhas):
    for i in range(1,10,2):
        print(' '* linhas + i * '*')
        linhas = linhas-1


linhas = 9

res = triangulo(linhas)

print(res)
