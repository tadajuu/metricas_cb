import math
dist_a=float(input("Distancia a: "))
dist_b=float(input("Distancia b : "))
ang=float(input("Digite o angulo de Y: "))

ang_rad=math.radians(ang)

c=math.sqrt(dist_a**2+dist_b**2-2*dist_a*dist_b*math.cos(ang_rad))

print(round(c,2))
