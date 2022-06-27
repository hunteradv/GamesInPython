print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

secret_number = 10
attempts = 3

for actual_round in range(1, attempts + 1):
    print("Tentativa {} de {}".format(actual_round, attempts))
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

print("Fim do jogo")
