o=input()
a=[]
r=int(12)
c=int(12)
sum=int(0)
for i in range(r):
    b = []
    for j in range(c):
        n=float(input())
        b.append(n)
    a.append(b)

for i in range(r-1):
    for j in range(c):
        sum=a[i][j]+sum
     c=c-1
if o=='S':
    print("%.1f"%sum)
else:
    avg=float(sum/66.0)
    print("%.1f" % avg)
