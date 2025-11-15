ml = float(input("Qual a nota média dos laboratórios? "))
mt = float(input("Qual a nota média dos trabalhos? "))
mp = float(input("Qual a nota média das provas? "))

nf = (ml*(1/4)) + (mt*(3/10)) + (mp*(45/100))

print(round(nf,2))