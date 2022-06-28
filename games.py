import gallow
import guessing

print("****************")
print("Escolha seu jogo")
print("****************")

print("(1) Forca (2) Adivinhação")
game = int(input("Qual jogo?"))

if game == 1:
    print("Jogando forca")
elif game == 2:
    print("Jogando Adivinhação")

print("fim do jogo!")
