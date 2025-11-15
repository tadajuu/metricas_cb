vol = float(input("Volume consumido durante o mes: "))
m3 = 0.37
taxad = 15
icms = ((vol*m3)+taxad)*(35/100)
total = ((vol*m3)+taxad)+icms
print(round(total,2))