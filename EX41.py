def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
    if b !=0:
        a/b
    else:
        print("valor invalido")
escolha=""
while escolha!="0":          
    num1=int(input("digite o primeiro numero"))
    num2=int(input("digite o segundo numero"))        
    escolha=input("digite uma opção 0-parar,1-somar, 2-subtrair, 3-multiplicar, 4-dividir")  
    if escolha=="1":
                x=somar(num1,num2)
    elif escolha=="2":
                x=subtrair(num1, num2)
    elif escolha=="3":
                x=mult(num1, num2)
    else:
                x=div(num1, num2)
print(f" resultadoda operação:{x}")                        

num1=int(input("digite o primeiro numero"))
num2=int(input("digite o segundo numero"))
x=div(num1, num2)
print(f" resultado da operação:{x}")