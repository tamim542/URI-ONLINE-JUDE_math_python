while True:
    try:
        sum1 = int(1)
        sum2 = int(1)
        x = int(input())
        y = int(input())
        if x>=0 and x<=20:
            for i in range(1,x+1):
                sum1=sum1*i
        if y >= 0 and y <= 20:
            for i in range(1,y+1):
                sum2=sum2*i
        total=int(sum1+sum2)
        print(total)
    except EOFERROR:
        break

