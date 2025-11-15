quantidade = float(input())

totalSem = (quantidade * 2.86) + 50.00
totalCom = totalSem + totalSem*(34/100)

print ( round (totalCom,2))