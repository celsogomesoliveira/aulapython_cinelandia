#Crie uma função que receba o lado de um quadrado e retorne o valor da sua área($A=lado^2$)
def quadrado(lado):
    return lado ** 2
#usando o operador de exponenciação(**)
#interação com usuário
medida_lado=float(input("digite a medida do lado do quadrado:"))
#chamada da função e exibição do resultado
area=quadrado(medida_lado)
print(f" A área do quaadrado é:{area}")