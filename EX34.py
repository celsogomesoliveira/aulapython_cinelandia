# desenvolva um codigo python
# usando while que digite um nome
# e imprima, só pára o programa
# ao digitar sair em maisculo
# != diferente
nome=""
while nome != "SAIR":
    nome=input("digite um nome").upper()
    if nome=="SAIR":
        break #sai do laço while
    print(f"Seja bem vindo/a {nome}")




