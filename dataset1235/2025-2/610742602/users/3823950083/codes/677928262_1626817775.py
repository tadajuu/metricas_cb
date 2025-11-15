import math
radius = float(input("Informe o valor do raio em cm: "))

circum_area = math.pi * (radius ** 2)
circum_volum = math.pi * (4/3) * (radius ** 3) 

print (round(circum_area, 3))
print (round(circum_volum, 3))