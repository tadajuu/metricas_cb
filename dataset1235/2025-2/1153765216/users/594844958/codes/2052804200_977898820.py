renda = float(input())
prestacao = float(input())

if prestacao > (20/100) * renda:
  print("Emprestimo nao aprovado")
else:
  print("Emprestimo aprovado")