produto=input("Digite um produto").upper()
if(produto=="MOUSE"):
    preco=10
elif(produto=="TECLADO"):
    preco=20
elif(produto=="MEMORIA"):
    preco=100
else:
    preco=0
    print("Produto não existe")
qtd = int(input("Digite a quantidade"))   
total = preco * qtd
if(qtd>10):
    imposto = 0.05*total
else:
    imposto = 0.10*total
valorfinal = total + imposto
print (f"o valor final é de {valorfinal}")
print(f"produto=> {produto}")
print(f" Quantidade=> {qtd}")
print(f"Imposto=> {imposto}")

