#escreva um programa que solicite um determinado número de dias, em seguida exiba o quanto esses dias equivalem em horas, minutos e segundos
dias = int(input("Insira quantidade de dias:"))
horas = dias*60
minutos = horas*60
segundos = minutos*60
print("Horas:", horas, "minutos:", minutos, "segundos:", segundos)
