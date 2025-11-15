s = float(input("Qual o salário do seu madruga? "))
p = float(input("Qual o valor da aluguel? "))

if (0.2 * s) >= p:
  print("Emprestimo aprovado")
else:
  print("Emprestimo nao aprovado")