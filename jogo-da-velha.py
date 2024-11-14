import random

def minimax(tabuleiro, eh_max):
    vencedor_x = verifica_vencedor(tabuleiro, "X")
    vencedor_o = verifica_vencedor(tabuleiro, "O")

    if vencedor_x:
        return -1
    elif vencedor_o:
        return 1
    elif verifica_empate(tabuleiro):
        return 0

    if eh_max:
        melhor_pontuacao = -float('inf')
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                pontuacao = minimax(tabuleiro, False)
                tabuleiro[i] = " "
                melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                pontuacao = minimax(tabuleiro, True)
                tabuleiro[i] = " "
                melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

def movimento_minimax(tabuleiro):
    melhor_pontuacao = -float('inf')
    melhor_movimento = None
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            pontuacao = minimax(tabuleiro, False)
            tabuleiro[i] = " "
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = i
    return melhor_movimento

def movimento_oponente(tabuleiro, dificuldade):
    movimentos_disponiveis = [i for i, campo_tabuleiro in enumerate(tabuleiro) if campo_tabuleiro == " "]
    if dificuldade == "Fácil" and random.random() > 0.25:
        tabuleiro[random.choice(movimentos_disponiveis)] = "O"
    elif dificuldade == "Médio" and random.random() > 0.50:
        tabuleiro[random.choice(movimentos_disponiveis)] = "O"
    else:
        melhor_movimento = movimento_minimax(tabuleiro)
        if melhor_movimento is not None:
            tabuleiro[melhor_movimento] = "O"

def verifica_empate(tabuleiro):
    return " " not in tabuleiro

def verifica_vencedor(tabuleiro, jogador):
    possibilidades_vitoria = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in possibilidades_vitoria:
        if tabuleiro[a] == jogador and tabuleiro[b] == jogador and tabuleiro[c] == jogador:
            return True
    return False

def escolhe_jogada(tabuleiro):
    while True:
        try:
            move = int(input("Escolha sua jogada (1-9): ")) - 1
            if tabuleiro[move] == " ":
                tabuleiro[move] = "X"
                break
            else:
                print("Posição já ocupada! Escolha outra.")
        except (ValueError, IndexError):
            print("Entrada inválida. Escolha um número de 1 a 9.")

def mostra_tabuleiro(tabuleiro):
    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

def main():
    tabuleiro = [" "] * 9
    dificuldade = input("Escolha o modo de dificuldade (Fácil, Médio, Difícil): ")

    mostra_tabuleiro(tabuleiro)

    while True:
        escolhe_jogada(tabuleiro)

        mostra_tabuleiro(tabuleiro)

        if verifica_vencedor(tabuleiro, "X"):
            print("Parabéns! Você venceu!")
            break

        if verifica_empate(tabuleiro):
            print("Empate!")
            break

        movimento_oponente(tabuleiro, dificuldade)

        print("O oponente jogou!")

        mostra_tabuleiro(tabuleiro)

        if verifica_vencedor(tabuleiro, "O"):
            print("O oponente venceu!.")
            break

        if verifica_empate(tabuleiro):
            print("Empate!")
            break

main()