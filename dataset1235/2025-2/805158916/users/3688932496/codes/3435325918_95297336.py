escala = input("Escala:").upper()
temp_entrada = float(input("Informe o valor da temperatura:"))

if ( escala == 'C'):
    temp_saida = (9/5) * temp_entrada + 32
    print(round(temp_saida,2))
else:
    temp_saida = (5/9) * (temp_entrada - 32)
    print(round(temp_saida,2))