escala = input("escala").upper()
temp_entrada = float(input("valor: "))

if (escala == "C"):
  temp_saida = (9/5) * temp_entrada + 32

else:
  temp_saida = (5/9) * (temp_entrada - 32)

print(round(temp_saida, 2 ))



  
