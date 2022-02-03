k=int(input())
g=input()
a=[]
r=int(12)
c=int(12)
for i in range(r):
    b=[]
    for j in range(c):
        b.append(float(input()))
    a.append(b)
n=float(0.0)
for i in range(12):
    n=a[k][i]+n

if g == 'S':
    print("%.1f"%n)
elif g == 'M':
    avg=float(n/12.0)
    print("%.1f"%avg)
