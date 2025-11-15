tempo_estacionado = float(input())
valorppg= (tempo_estacionado  * 15) + 5
imposto = 20/100 * valorppg
valortot= valorppg + imposto

print(round(valortot,2))