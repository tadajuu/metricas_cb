xa = float(input("Xa: "))
ya = float(input("Ya: "))
xb = float(input("Xb: "))
yb = float(input("Yb: "))

dist = ((xb-xa)**2 + (yb-ya)**2)**(1/2)

print(round(dist, 3))