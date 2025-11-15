import math
da = float(input())
db = float(input())
ay = float(input())
graus = math.radians(ay)
c = math.sqrt(da**2+db**2-2*da*db*math.cos(graus))
print(round(c,2))