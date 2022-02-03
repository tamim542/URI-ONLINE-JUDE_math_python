x=int(input())
y=int(input())
j=int(0)
for i in range(1,y+1):
    j += 1
    print(i,end='')
    if x==j or i==y:
        print("\n")
        j=0
    else:
        print(end=' ')