peso = float(input("Peso de sua mercadoria (em kg):"))
delivery = (peso*43.21) + 25
realdelivery = delivery+ (62/100)*delivery
print(round(realdelivery,2))