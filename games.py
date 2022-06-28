import gallow
import guessing


def choice_game():
    print("****************")
    print("Escolha seu jogo")
    print("****************")

    print("(1) Forca (2) Adivinhação")
    game = int(input("Qual jogo? "))

    if game == 1:
        print("Jogando forca")
        gallow.play()
    elif game == 2:
        print("Jogando Adivinhação")
        guessing.play()

    print("fim do jogo!")


if __name__ == "__main__":
    choice_game()