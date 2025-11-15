renda = float(input())
prestacao = float(input())

if(prestacao > renda*(20/100)):
  print("Emprestimo nao aprovado")
else:
  print("Emprestimo aprovado")