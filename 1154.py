sum=int(0)
i=int(0)
while(1):
    n=int(input())
    if n<0:
        break
    i+=1
    sum=n+sum
avg=float(sum/i)
print("%.2f"%avg)