qtd_litros = float(input("Informe a quantidade de litros: "))

gas = 2.86

valor = gas * qtd_litros + 50.00

valor_com_imposto = valor + valor * (34/100)

valor_c_i_arredondado = round (valor_com_imposto, 2)

print (valor_c_i_arredondado)