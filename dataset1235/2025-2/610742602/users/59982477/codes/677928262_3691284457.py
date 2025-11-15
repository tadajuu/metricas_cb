#Lendo as quatro notas 
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
#Calculando q média ponderada 
media_ponderada = (nota1*1 + nota2*2 + nota3*3 + nota4*4) / (1+2+3+4)
#Imprimindo a média arredondada para duas casas decimais
print(round(media_ponderada, 2))
