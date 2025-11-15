soma = 0
for i in range(1,5):
  nota = float(input())
  soma = soma + nota*i

media = soma / 10
print(round(media,2))