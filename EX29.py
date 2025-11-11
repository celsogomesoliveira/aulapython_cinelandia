#desenvolva um codigo python que
#leia 5 numeros e diga se cada
#numero ao momento que for lido
#se é par ou impar
for i in range (0,5):
    n=int(input("digite um valor "))
    if n % 2 ==0:
        print(f"o valor  {n} é par")
    else:
        print(f"o valor  {n} é impar")
