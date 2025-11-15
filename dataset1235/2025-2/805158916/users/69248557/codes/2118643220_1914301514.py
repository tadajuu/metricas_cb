consumo = float(input("Informe o consumo de chamadas por min "))

valorp = (consumo * 0.28) + 23
aumento = (1+0.31)*valorp
print(round(aumento,2))