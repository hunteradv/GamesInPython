from random import random, randrange

print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

secret_number = randrange(1, 101)
attempts = 0
option = False

while option is False:
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    level = int(input("Digite o nível: "))

    if level == 1:
        attempts = 20
    elif level == 2:
        attempts = 10
    elif level == 3:
        attempts = 5
    else:
        print("Necessário definir o número de 1 a 3")

    if level == 1 or level == 2 or level == 3:
        option = True

for actual_round in range(1, attempts + 1):
    print("Tentativa {} de {}".format(actual_round, attempts))
    guess = int(input("Digite um número de 1 a 100: "))
    print("")
    print("Você digitou ", guess)

    if guess < 1 or guess > 100:
        print("Você deve digitar um número de 1 a 100!")
        print("")
        continue

    bigger = guess > secret_number
    smaller = guess < secret_number

    if smaller:
        print("Você errou! Seu chute foi menor que o número secreto")
        print("")
    elif bigger:
        print("Você errou! Seu chute foi maior que o número secreto")
        print("")
    else:
        print("Você acertou!")
        break

print("Fim do jogo")
