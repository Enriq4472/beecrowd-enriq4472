numero=int(input())
print(numero)

print("%d nota(s) de R$ 100,00" %(int(numero/100)))

numero=numero%100
print("%d nota(s) de R$ 50,00" %(int(numero/50)))

numero=numero%50
print("%d nota(s) de R$ 20,00" %(int(numero/20)))

numero=numero%20
print("%d nota(s) de R$ 10,00" %(int(numero/10)))

numero=numero%10
print("%d nota(s) de R$ 5,00" %(int(numero/5)))

numero=numero%5
print("%d nota(s) de R$ 2,00" %(int(numero/2)))

numero=numero%2
print("%d nota(s) de R$ 1,00" %(int(numero/1)))
