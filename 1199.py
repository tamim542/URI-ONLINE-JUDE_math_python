from array import  *
hexadecimal =array('b',[])
decimal=int(input())
quotient =  decimal
j=int(0)
r=int(0)
while quotient != 0:
    remainder = quotient % 16
    if remainder < 10:
        j +=1
        r=int(r+48 + remainder)
        hexadecimal.insert(j, str(r))
        print(r)
    else:
        j +=1
        hexadecimal.insert(j, 55 + remainder)
    quotient = quotient / 16
    print( quotient)
print( hexadecimal)
