n = float(input())
r1 = n * 0.27
r2 = n * 1.42 
r3 = n * (1 - 0.63)
print((f"{r1: .2f}").rstrip('0').rstrip('.'))
print((f"{r2: .2f}").rstrip('0').rstrip('.'))
print((f"{r3: .2f}").rstrip('0').rstrip('.'))