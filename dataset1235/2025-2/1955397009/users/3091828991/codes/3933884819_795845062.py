medialab = float(input("media dos laboratorios: "))
mediatrab = float(input("media dos trabalhos: "))
mediaprov = float(input("media das provas: "))

ML = medialab*(25/100)
MT = mediatrab*(30/100)
MP = mediaprov*(45/100)

NF = (ML + MT + MP)

print(round(NF, 2))