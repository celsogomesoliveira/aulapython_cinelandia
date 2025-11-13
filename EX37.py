soma_positivos=0
numero=-1
while numero!=0:
    entrada=input("digite um numero (0 para parar):")
    try:
        numero=int(entrada)
    except ValueError:
        print("Entrada invalida. Digite um numero inteiro")
        continue
    if numero>0:
        soma_positivos=soma_positivos+numero
print(f"a soma dos numeros positivos digitados é: {soma_positivos}")            