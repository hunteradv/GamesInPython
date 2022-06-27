from random import random, randrange

print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

secret_number = randrange(1, 101)
attempts = 3

for actual_round in range(1, attempts + 1):
    print("Tentativa {} de {}".format(actual_round, attempts))
    guess = int(input("Digite um número de 1 a 100: "))
    print("Você digitou ", guess)

    if guess < 1 or guess > 100:
        print("Você deve digitar um número de 1 a 100!")
        continue

    bigger = guess > secret_number
    smaller = guess < secret_number

    if smaller:
        print("Você errou! Seu chute foi menor que o número secreto")
    elif bigger:
        print("Você errou! Seu chute foi maior que o número secreto")
    else:
        print("Você acertou!")
        break

print("Fim do jogo")
