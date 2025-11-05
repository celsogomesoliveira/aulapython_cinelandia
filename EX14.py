#desenvolva um codigo python que
#verifique se a temperatura esta frio, agradavel ou calor
#siga a tabela abaixo
#menor que 18 - frio
#entre 18 e 30 - agradavel
#maior que 30 - calor
v1= float (input("digite um valor"))
if (v1<=18):
    print (f"frio")
elif (v1>=30):
    print (f"calor")
else:
    print ("agradavel")