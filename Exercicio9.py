def volume_cilindro(raio,altura):
    volume = altura * 3.14 * (raio ** 2) 
    
    return volume


altura = int(input("Digite o VAlor Correspondente a Altura do Cilindro: "))
raio = int(input("Digite o VAlor Correspondente a Raio do Cilindro: "))

res = volume_cilindro(raio,altura)

print(f"O Volume do Cilintro é Correspondente a: {res}")