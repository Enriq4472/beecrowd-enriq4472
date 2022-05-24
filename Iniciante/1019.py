entrada=int(input())

horas=int(entrada/3600)
minutos=int((entrada%3600)/60)
segundos=int(((entrada%3600)%60))

print("%d:%d:%d" %(horas, minutos, segundos))
