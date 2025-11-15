var_a = float(input("Insira um número real: "))
var_b = float(input("Insira um número real: "))
var_c = float(input("Insira um número real: "))

num = a**2 + b**2 + c**2

den = a + b + c

frac = num/den

frac_arredondado = round(frac, 7)

print(frac_arredondado)