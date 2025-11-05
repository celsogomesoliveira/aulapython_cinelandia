#desenvolva um codigo python que leia
#um cargo de funcionário, de acordo com o cargo
#mostre o salário
#vide tabela abaixo
#caixa-1500
#vendedor-2400
#gerente-4000
#de acordo com os salários acima, calcule:
#inss = 12% sobre o salário
#irrf se o salario for maior que 2000 o irrf será de 14%
#sobre o salário senão será de 8%
#salário fina = salário - irrf - inss
v1=float(input ("digite um valor" ))
if (v1==4000):
    print (f" {v1} é um gerente" )
if (v1==1500):
    print(f" {v1} é um caixa" )
if (v1==2400):
    print(f" {v1} é um vendedor")    
v2=float(input "digite um valor")
    