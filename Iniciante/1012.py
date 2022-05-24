l=input()
l=l.split(' ')
A=float(l[0]); B=float(l[1]); C=float(l[2])
print("TRIANGULO: %.3F\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(((A*C)/2), (3.14159*C*C), (((A+B)/2)*C), (B*B), (A*B)))
