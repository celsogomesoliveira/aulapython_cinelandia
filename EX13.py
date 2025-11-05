#desenvolva um código python que leia 3 valores
#e mostre qual o maior
v1=float (input ("digite um valor"))
v2=float (input ("digite um valor"))
v3=float (input ("digite um valor"))
if (v1>v2 and v1>v3):
    print (f"{v1} é maior")
elif (v2>v1 and v2>v3):
    print (f"{v2} é maior")
else: 
    print (f"{v3}) é maior")
