# Use este codigo como ponto de partida

# Leitura de valores de entrada e conversao para inteiro
num = int(input("Digite um número"))

def get_double(value: int) -> int:
  return value * 2

# Impressao do dobro do numero
result = get_double(num)
print(result)