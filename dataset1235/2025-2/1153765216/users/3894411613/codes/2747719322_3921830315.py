litros = float(input("litros abastecidos: "))

vl = 2.86
ptrocadeoleo = 50.00
percentualicms = 34 / 100

vlcombustivel = litros * vl 
vlbruto = vlcombustivel + ptrocadeoleo
vltotalicms = vlbruto * percentualicms
vltotal = vlbruto + vltotalicms
print(round(vltotal , 2))