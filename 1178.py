a=[]
x=float(input())
for i in range(100):
    n=float(x)
    a.append(n)
    x=x/2
for i in range(100):
    print("N[",end='')
    print(i,end='')
    print("] = ",end='')
    print("%.4f"%a[i])