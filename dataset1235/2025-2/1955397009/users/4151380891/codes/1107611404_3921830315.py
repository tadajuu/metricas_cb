litros = float(input("quantidade de litros:"))
valorL = litros * 2.86
troca = 50
servico = valorL + troca 
icms = servico * 34/100

print(round(servico + icms, 2))