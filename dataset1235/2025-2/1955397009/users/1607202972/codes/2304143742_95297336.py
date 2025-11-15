x=input()
temp=float(input())
if(x=="C"):
  tempf=(9/5)*temp+32
else:
  tempf=(temp-32)/(1.8)
print(round(tempf,2))