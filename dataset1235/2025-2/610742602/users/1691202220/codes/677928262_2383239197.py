import math
A = float(input("Digite a distância A entre o observador e a primeira arvore: "))
B = float(input("Digite a distância B entre o observador e a segunda arvore: "))
gamma_graus = float(input("Digite o ângulo Y entre A e B (em graus): "))

gamma_rad = math.radians(gamma_graus)

CC = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(gamma_rad))

CC_rounded = round(CC, 2)

print(f'A distância entre as duas arvores é: {CC_rounded} ')