from math import sqrt
l1=input()
l2=input()

l1=l1.split(' ')
l2=l2.split(' ')

x1=float(l1[0])
x2=float(l2[0])
y1=float(l1[1])
y2=float(l2[1])

distancia=sqrt(((x2-x1)**2)+((y2-y1)**2))
print("%.4f" %(distancia))
