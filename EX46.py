#Crie uma função que receba dois números e retorne o maior deles.
def numero(a,b):
    return (a>b) and (a<b)
a=float(input("digite um numero:"))
b=float(input("digite um numero:"))
if a>b:
    print(f" O numero maior é {a}")
else: 
    print(f" O numero maior é {b}")   
