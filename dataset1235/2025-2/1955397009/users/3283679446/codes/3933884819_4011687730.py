# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

var_a = float(input("Insira um número real: "))
var_b = float(input("Insira um número real: "))
var_c = float(input("Insira um número real: "))

num = a**2 + b**2 + c**2

den = a + b + c

frac = num/den

frac_arredondado = round(frac, 7)

print(frac_arredondado)