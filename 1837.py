a=int(input())
b=int(input())
if a<0:
    e=int(b)
    if b<0:
        e=b * -1
    for r in range(e):
        f=int(a-r)
        if f%b==0:
            break;
    q=int(f/b)
else:
    q=int(a/b)
    r=int(a%abs(b))
print("\n",q,r)
#print(end=' ')
