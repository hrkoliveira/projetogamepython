import random
from os import system, name

#Função para limpar a tela a cada execução.

def limpa_tela():
    #windonws
    if name == 'nt':
        _= system('cls')

    # mac ou linux
    else:
        _= system('clear')


# Função

def game():
    limpa_tela()

    print("\nBem vindo (a) ao jogo da forca")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # list comprehension
    letras_descobertas = ['_' for letra in palavra]

    # numeros de chances
    chances = 6

    # lista para as letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero.

    while chances >= 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1


        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)



        # bloco main 
if __name__ == "__main__":
    game()
    print("\nParabéns, voc~e está aprendendo a programar\n")