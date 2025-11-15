horas = int(input())

valorSemImposto = 15 * horas + 5
valorTotal = valorSemImposto * (20/100) + valorSemImposto

print(round(valorTotal, 2))