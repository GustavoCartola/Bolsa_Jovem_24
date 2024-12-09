    import random

    # Random number between 1 and 10
    secret_number = random.randint(1, 10)

    print("Adivinhe o número entre 1 e 10!")

    # User attempts
    for attempt in range(3):
        guess = int(input("Digite seu palpite: "))

        if guess == secret_number:
            print("Parabéns! Você acertou!")
            break
        elif guess < secret_number:
            print("O número é maior!")
        else:
            print("O número é menor!")

    else:
        print(f"Você perdeu! O número era {secret_number}.")
