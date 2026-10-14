n=int(input())
temp=n
total=0
power=len(str(n))
while temp>0:
  digit=temp%10
  total=total+digit**power
  temp=temp//10
if n==total:
  print("Amstrong")
else:
  print("Not Amstrong")
