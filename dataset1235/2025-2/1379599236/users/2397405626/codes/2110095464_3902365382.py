# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

tempo = float(input("Informe o tempo de viagem em horas: "))
velocidade = float(input("Informe a velocidade media do veiculo: "))

distancia = velocidade*tempo
litros = distancia//12

print(distancia)
print(litros)