peso_do_saco = float(input("digite um valor: "))
quantidade_diaria = float(input("digite um valor: "))
quantidade_em_grama = peso_do_saco - (quantidade_diaria * 7)
print(round(quantidade_em_grama, 4))