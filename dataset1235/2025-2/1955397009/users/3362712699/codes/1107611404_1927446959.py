n = float(input("Qual o número real que você quer calcular a porcentagem?: "))

p = float(n * (27 / 100))
q = float(n + n * (42 / 100))
r = float (n - n * (63 / 100))

print(float(round(p, 2)))
print(float(round(q, 2)))
print(float(round(r, 2)))