import math # puxando a biblioteca da matemática
r = float(input("Digite o seu raio: "))
area_circulo = math.pi * r ** 2
volume_circulo = (4/3) * math.pi * r ** 3
area_circulo_arredondamento = round(area_circulo, 3)
volume_circulo_arredondamento = round(volume_circulo, 3)
print(area_circulo_arredondamento)
print(volume_circulo_arredondamento)
                 