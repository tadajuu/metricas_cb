prova_1= float(input("Nota da prova 1:"))
prova_2=float(input("Nota da prova 2:"))
prova_3=float(input("Nota da prova 3:"))
prova_4=float(input("Nota da prova 4:"))

media_ponderada=((prova_1*1)+(prova_2*2)+(prova_3*3)+(prova_4*4))/(1+2+3+4)

print (round(media_ponderada,2))