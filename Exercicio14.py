def consumo(distancia,quantidade):
    consumo_kml = distancia / quantidade
    if consumo_kml < 8:
        print(consumo_kml)
        print("Gasta muito!")

    if consumo_kml >= 8 and consumo_kml <= 15:
        print(consumo_kml)
        print("Econômico!")

    if consumo_kml > 15:
        print(consumo_kml)
        print("Super econômico!")



distancia = int(input("Digite a Distância em Km: "))
quantidade = int(input("Digite a Quantidade de Litros de Gasolina Existente no Veiculo: "))

res = consumo(distancia,quantidade)

print(res)