entrada=int(input())

anos=int(entrada/365)
meses=int((entrada%365)/30)
dias=int(((entrada%365)%30))

print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(anos, meses, dias))
