from math import cos, radians

a=float(input())
b=float(input())

ang_y=float(input())
ang_y_rad=radians(ang_y)
cos_y=cos(ang_y_rad)

c=(a**2+b**2-2*a*b*cos_y)**(1/2)

print(round(c,2))



