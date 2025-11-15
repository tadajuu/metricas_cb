alimento = input()
alimento.upper()

quantidade_alimento = int(input())
quantidade_refrigerantes = int(input())

valor_disponivel = float(input())

if alimento == "B":
  valor_total = (2.50 * quantidade_alimento) + (3 * quantidade_refrigerantes)

elif alimento == "S":
  valor_total = (3.50 * quantidade_alimento) + (3 * quantidade_refrigerantes)

print(f"{round(valor_total, 2)}")

if valor_disponivel >= valor_total:
  print("Sim")
else:
  print("Nao")