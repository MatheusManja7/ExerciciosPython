def calculu(horas,minutos,segundos):
    horas_em_segundos = 60 * (horas * 60)
    minutos_em_segundos = minutos * 60
    segundoss = segundos
    
    print("<------------------------------------------->")
    print(f"{horas} Hora corresponde a {horas_em_segundos} Segundos")
    print(f"{minutos} Minuto corresponde a {minutos_em_segundos} Segundos")
    print(f"{segundoss} Segundos")

print()
horas = int(input("Digite um Valor Correspondente a Horas: "))    
minutos = int(input("Digite um Valor Correspondente a minutos: "))    
segundos = int(input("Digite um Valor Correspondente a segundos: "))    

valores = calculu(horas,minutos,segundos)