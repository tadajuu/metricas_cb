nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

num = nota1 + nota2 * 2 + nota3 * 3 + nota4 * 4

quo = num/10

quo_arredondamento = round (quo, 2)

print (quo_arredondamento)