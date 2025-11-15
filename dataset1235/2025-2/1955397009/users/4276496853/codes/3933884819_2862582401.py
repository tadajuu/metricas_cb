# Leitura das entradas
nome_do_objeto = input()
repeticoes = int(input())

# Montagem da frase mágica
frase = "Abra " + nome_do_objeto + " "

# Impressão do feitiço repetido N vezes (sem espaço extra no final)
print((frase * repeticoes).strip())
