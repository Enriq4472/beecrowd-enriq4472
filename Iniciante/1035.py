l=input()
l=l.split(' ')
A=int(l[0])
B=int(l[1])
C=int(l[2])
D=int(l[3])
if (B>C and D>A and C+D>A+B and C>0 and D>0 and A%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
