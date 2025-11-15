tf=float(input())
tx= tf*0.28
vf=23.00
icms= (tx+vf) * (31/100)
vpm= (tx+vf+icms)
print (round(vpm,2))
