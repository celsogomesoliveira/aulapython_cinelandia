import random

# --- Variáveis de Controle ---
vitorias_usuario = 0
vitorias_computador = 0
empates = 0

opcoes = ['pedra', 'papel', 'tesoura']

print("--- JOGO: PEDRA, PAPEL, TESOURA ---")
print("O jogo continua até você vencer 3 rodadas!")

# --- Loop Principal do Jogo ---
# O loop continua enquanto o usuário não tiver 3 vitórias
while vitorias_usuario < 3:
    print("\n------------------------------")
    print(f"PLACAR ATUAL: Você {vitorias_usuario} x {vitorias_computador} Computador | Empates: {empates}")
    
    # 1. Pede a entrada do usuário
    escolha_usuario = input("Escolha (Pedra, Papel ou Tesoura): ").strip().lower()
    
    # 2. Escolha do computador (aleatória)
    escolha_computador = random.choice(opcoes)

    # 3. Verifica a entrada do usuário
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Por favor, digite 'pedra', 'papel' ou 'tesoura'.")
        continue  # Volta para o início do loop

    print(f"Você escolheu: {escolha_usuario.capitalize()}")
    print(f"O computador escolheu: {escolha_computador.capitalize()}")
