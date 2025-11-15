vproduto = float(input())
taxa = 15
imposto = 0.30
vpago = float((vproduto + taxa))
vacrescimo = float((vpago*imposto))

valortotal = vpago + vacrescimo
print(round(valortotal, 2))