gasolina = 2.86
custo_oleo = 50.00
icms = 34

litro_abastecido = float(input("resultado"))
valor_abs = litro_abastecido * gasolina
servico = valor_abs + custo_oleo
valor_do_icms = servico * 34/100
pagar = servico + valor_do_icms

print(round(pagar, 2))

