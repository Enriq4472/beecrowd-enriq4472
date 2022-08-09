from math import sqrt

v=input()
v=v.split(' ')

A=float(v[0])
B=float(v[1])
C=float(v[2])

d =( B*B - 4*A*C )

if (d<=0 or A==0):
    print("Impossivel calcular")
else:
    print("R1 = %.5f" %( (-1)*B + ( sqrt(d) )) )
    print("R2 = %.5f" %( (-1)*B - ( sqrt(d) )) )
