print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

secret_number = 42
attempts = 3
actual_round = 1

while actual_round <= attempts:
    print("Tentativa ", actual_round, "de ", attempts)
    guess = int(input("Digite o seu número: "))
    print("Você digitou ", guess)

    bigger = guess > secret_number
    smaller = guess < secret_number

    if smaller:
        print("Você errou! Seu chute foi menor que o número secreto")
    elif bigger:
        print("Você errou! Seu chute foi maior que o número secreto")
    else:
        print("Você acertou!")

    actual_round = actual_round + 1


print("Fim do jogo")
