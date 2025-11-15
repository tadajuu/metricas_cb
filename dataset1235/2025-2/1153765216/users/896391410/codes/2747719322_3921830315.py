gasolina = 2.86
custo_oleo = 50.00
icms = 34

litro_abastecidos = float(input("Digite o litro:"))
valor_abs = litro_abastecidos * gasolina
servico = valor_abs + custo_oleo
valor_do_icms = servico * (icms/100)

pagar = servico + valor_do_icms

print(round(pagar , 2))