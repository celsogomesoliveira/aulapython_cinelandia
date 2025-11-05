#estudo de caso:
#voce foi contratado pelo exercito brasileiro para desenvolver um alistamento militar
#onde se le o ano de nascimento do candidato e o genero
#o sistema ira calcular a idade
#se a idade for maior ou igual a 18 e o sexo masculino estara apto a se alistar
#senão não esta apto
anonasc=int(input("Digite o ano de nascimento"))
genero= input ("Digite M ou F").upper()
#print(anonasc)
#print(genero)
idade=2025-anonasc
if(idade >=18 and genero == "M"):
    print("apto a se alistar")
else:
    print("não apto")  
 


