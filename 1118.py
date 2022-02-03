ar=[]
while True:
    j=0
    for i in range(100):
        n=float(input())
        if n >= 0.0 and n <= 10.0 :
            ar.insert(j,n)
            j+=1
        else :
            print("nota invalida")
        if j==2 :
            avg = (ar[0]+ar[1])/2
            print("media = %.2f"%avg)
            break
    for l in range(100):
        X=float(input())
        print("novo calculo (1-sim 2-nao)")
        if X==1 or X == 2 :
            break
    if X==1 :
        continue
    if X==2:
        break

