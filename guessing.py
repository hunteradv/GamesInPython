print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

secret_number = 42

guess = int(input("Digite o seu número: "))

print("Você digitou ", guess)

if guess != secret_number:
    print("Você errou")
else:
    print("Você acertou!")

print("Fim do jogo")
