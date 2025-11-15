saco = int(input("Peso do saco da racao: "))
racaodiaria = float(input("Quantidade de racao diaria: "))
restante = saco - 7 * racaodiaria
print(round(restante, 2))
