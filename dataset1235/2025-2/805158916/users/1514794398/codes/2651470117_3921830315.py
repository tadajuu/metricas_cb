lgas= float(input("quantidade abastecida : "))

pgas=2.86

oleo=50

valorgas=lgas*pgas 

vservico=valorgas+oleo

valortotal=vservico*(1+34/100)

print(round(valortotal,2))