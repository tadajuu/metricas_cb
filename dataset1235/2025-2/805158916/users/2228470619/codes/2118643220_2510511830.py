min = float(input("Informe a quantidade de minutos excedentes: "))
valor1 = 45+(0.97*min)
valor_final = valor1+(valor1*(42/100))
print("O valor final a ser pago é: ",round(valor_final,2))