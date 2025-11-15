# v = entrada está sendo transformada em somente letras maiúsculas 
#por conta das condições aceitar somente em maiusculas
entrada = input().upper()
temp = float (input())


if (entrada=="C"): #condição que indica a entrada de celcius para fahrenheit
  conversao = (9/5)*temp + 32 #calculo da condição
  print(round( conversao,2 )) 

elif (entrada=="F"): #condição que indica a entrada de fahrenheit para celcius
  conversao=(5/9)*(temp-32) #calculo da condição
  print(round(conversao,2))

else: # saída somente ativada quando n usada C or F
  print("entrada errada")




  



