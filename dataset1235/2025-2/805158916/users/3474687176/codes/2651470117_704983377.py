#ler 2 números inteiros x=dvidendo y=divisor
dividendo = int(input(''))
divisor = int(input(''))

#parte inteira
quociente = int(dividendo / divisor)
resto = (dividendo % divisor)

#parte real
quocienteReal = float(dividendo / divisor)

#produto de x*y
produto = (dividendo * divisor)

#y**3
yAoCubo = (divisor**3)

#prints
print(quociente , resto)
print(quocienteReal)
print(produto , yAoCubo)