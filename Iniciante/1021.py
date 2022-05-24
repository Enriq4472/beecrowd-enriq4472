entrada=float(input())

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %(int(entrada/100)))

entrada=entrada%100
print("%d nota(s) de R$ 50.00" %(int(entrada/50)))

entrada=entrada%50
print("%d nota(s) de R$ 20.00" %(int(entrada/20)))

entrada=entrada%20
print("%d nota(s) de R$ 10.00" %(int(entrada/10)))

entrada=entrada%10
print("%d nota(s) de R$ 5.00" %(int(entrada/5)))

entrada=entrada%5
print("%d nota(s) de R$ 2.00" %(entrada/2))

print("MOEDAS:")
entrada=entrada%2
print("%d moeda(s) de R$ 1.00" %(entrada/1))

entrada=entrada%1
print("%d moeda(s) de R$ 0.50" %(entrada/0.5))

entrada=entrada%0.5
print("%d moeda(s) de R$ 0.25" %(entrada/0.25))

entrada=entrada%0.25
print("%d moeda(s) de R$ 0.10" %(entrada/0.1))

entrada=entrada%0.1
print("%d moeda(s) de R$ 0.05" %(entrada/0.05))

entrada=entrada%0.05
print("%d moeda(s) de R$ 0.01" %(entrada/0.01))
