peso = float(input("digite o peso do saco de racao em gramas:"))
diaria = float(input("digite a quantidade diaria de racao em gramas:"))
restante = peso-(5*diaria)
print(round(restante, 3))