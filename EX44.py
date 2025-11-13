def ehpar(numero):
    return numero % 2 == 0
num=int(input("digite um numero inteiro:"))
resultado=ehpar(num)
if resultado:
    print(f" O numero {num} é par.")
else:
    print(f" O numero {num} é impar.")

