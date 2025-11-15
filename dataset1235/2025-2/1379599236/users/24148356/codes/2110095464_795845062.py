ML = float(input("Média_dos_laboratórios: "))
MT = float(input("Média_dos_trabalhos: "))
MP = float(input("Média_das_provas: "))

ML = ML * 0.25
MT = MT * 0.30
MP = MP * 0.45

M = (ML + MT + MP)

print(round(M, 2))