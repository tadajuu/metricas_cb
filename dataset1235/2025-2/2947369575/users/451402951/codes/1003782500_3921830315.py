litros = float(input())

gasolina = 2.86
servico = 50.0
icms = 34

valor_abastecimento = litros * gasolina

total_sem_imposto = valor_abastecimento + servico

valor_icms = total_sem_imposto * (icms / 100)

total_com_imposto = total_sem_imposto + valor_icms

print(round(total_com_imposto, 2))