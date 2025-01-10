def volume_es(raio):
    calculo1 = (4 * 3.14) * (raio ** 3)
    volume = calculo1 / 3
    print(f"{volume:.2f}")

raio = int(input("Digite o VAlor Correspondente ao Raio da Esfera: "))


res = volume_es(raio)