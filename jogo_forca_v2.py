# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Import
import random
from os import system, name

# Função para limpar a tela
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

# Função que desenha a forca
def display_hangman(chances):
    stages = [  
                # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Função principal do jogo
def game():
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)
    lista_letras_palavras = list(palavra)
    tabuleiro = ["_"] * len(palavra)
    chances = 6
    letras_tentativas = []
    
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", " ".join(tabuleiro))
        print("\nLetras tentadas:", ", ".join(letras_tentativas))
        
        tentativa = input("\nDigite uma letra: ").lower()
        
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra!")
            continue
            
        letras_tentativas.append(tentativa)
        
        if tentativa in lista_letras_palavras:
            for i in range(len(lista_letras_palavras)):
                if lista_letras_palavras[i] == tentativa:
                    tabuleiro[i] = tentativa
                    
            if "_" not in tabuleiro:
                print("\nParabéns. Você venceu!!!. :) A palavra era:", palavra)
                return  # Sai da função imediatamente após vitória
        else:
            chances -= 1
            print("Ops. Essa letra não está na palavra!")
    
    # Só executa se esgotar as chances
    print(display_hangman(chances))
    print("\nVocê perdeu! A palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
    game()
    # Removido o print extra de parabéns