def convert_to_new_zeland_dolars_to_reais (reais: float) -> float:
  return reais * 2.96

new_zeland_dolars = int(input())

result = convert_to_new_zeland_dolars_to_reais(new_zeland_dolars)
print(round(result,2))

