n=int(input())
for j in range(1,n+1):
    c=int(0)
    a = int(input())
    b = int(input())
    ac=float(input())
    bc=float(input())
    while b >= a:
        a *=int  (ac/ 100)+1
        b *=int (bc )/ 100+1
        c +=1
    if c > 100:
        print("Mais de 1 seculo.")
        break
    if c<=100:
        print(c," anos.")

