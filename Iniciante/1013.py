l=input()
l=l.split(' ')
n1=int(l[0]); n2=int(l[1]); n3=int(l[2])
print("%d eh o maior" %((((n1+n2+abs(n1-n2))/2)+n3+abs(((n1+n2+abs(n1-n2))/2)-n3))/2))
