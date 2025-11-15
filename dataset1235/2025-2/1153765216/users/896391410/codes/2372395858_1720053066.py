saco = float(input("Digite o saco:"))
quantidade_diaria = float(input("Digite a quantidade:"))
quantidade_semanal = quantidade_diaria * 6
resto = saco - quantidade_semanal

print(round(resto, 4))

