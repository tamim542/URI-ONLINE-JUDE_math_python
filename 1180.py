X=[]
m=0
N=int(input())
for i in range(N):
    x=int(input())
    X.append(x)
    min=X[0]
for i in  range(N):
    if min>X[i] :
        min=X[i]
        m=i
print("Menor valor: %d" % min)
print("Posicao: %d" % m)
