def trianguloLateral(linhas):
    for i in range(linhas):
        print("*" * (i + 1))

    for j in range(linhas):
        print("*" * (linhas - j - 1))    


linhas = 4   

res = trianguloLateral(linhas)

print(res)