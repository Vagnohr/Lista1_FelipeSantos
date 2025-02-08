#escreva um programa que pergunta o valor total da conta e em seguia pergunte quantos clientes existem, divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "cada cliente deve pegar:" xvalor
conta = int(input("Qual o valor total da conta?  "))
clientes = int(input("Quantos clientes?  "))
valorpago = conta/clientes
print ("Cada cliente deve pagar", valorpago)