e=[]
a=input()
p=int(0)
w=float(0.0)
r=int(6)
c=int(6)
for i in range(r):
    d=[]
    for j in range(c):
        n=float(input())
        d.append(n)
    e.append(d)
for z in range(1,4):
    if z<=2:
        for v in range(p):
            w=e[z][v]+w
        p+=1
    if z>=3:
        for v in range(r):
            w=e[z][v]+w
            print("r=",r)
        r-=1
if a=='S':
    print("%.1f"%w)
elif a=='M':
    avg=w/30.0
    print("%.1f"%avg)