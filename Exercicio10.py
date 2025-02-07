#escreva um programa que pergunte quantos pedaços o bolo tem, em seguida pergunte quantos pedaços ele comeu, calcule quantos pedaços ainda tem e exiba o resultado com uma mensagem de livre escolha
bolo = int(input("Quantos pedaços o bolo tem?  "))
comeu = int(input("QUantos pedaços você comeu?  "))
restante = bolo-comeu
print("O bolo tem", bolo, ", você comeu", comeu, ", restaram", restante)