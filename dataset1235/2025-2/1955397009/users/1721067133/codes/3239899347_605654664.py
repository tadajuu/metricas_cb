peso = float(input())

valorFrete = ((peso*43.21) + 25)
valorTotal = valorFrete + ((62/100)*valorFrete)

print(round(valorTotal,2))