n=int(input())
j=int(0)
for i in range(1000):
    print("N[",end='')
    print(i,end='')
    print("] = ",end='')
    print(j)
    j=j+1
    if j==n:
        j=0;
