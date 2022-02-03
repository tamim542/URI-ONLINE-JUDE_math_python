s=float(0)
j=int(1)

for i in range(1,40,+2):
    s = s + (i/j)
    j = j+j
print("%.2f"%s)


