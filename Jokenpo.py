import random
print("\tJOGO DO PAPEL PEDRA TESOURA")
user = str(input("Nome do jogador: "))  # prompt for the player's name

def menu():
    option = True
    while option:
        print("\t\tMenu")
        print("""
            1. Continuar a jogar
            2. Exit/Quit/Saída """)
        option = input("Escolha uma opção:  ")
        if option == "1":
            game()  # start the game
        elif option == "2":
            print("\n Adeus")  # say goodbye
            option = None
        else:
            print("\n Escolha não válida.\n Tente outra vez.")  # invalid choice message

def game():
    print("\n\n\t\t [1] - Pedra\n\t\t [2] - Tesoura\n\t\t [3] - Papel\n ")
    valid_choice = True
    while valid_choice:
        player_choice = str(input("Escolha uma opção (escreva a palavra): "))
        move = player_choice.lower().capitalize()
        if player_choice == 'pedra' or player_choice == 'papel' or player_choice == 'tesoura':
            choices = ["Pedra", "Tesoura", "Papel"]
            computer_choice = random.choice(choices)
            print("O Computador jogou: ")
            if computer_choice == move:
                print("O computador jogou {} e o {} jogou {}".format(computer_choice, user, move))
                print("Empate")
                menu()
            elif computer_choice == "Pedra" and move == "Tesoura":
                print("O Computador Ganhou\n")
                print("O computador jogou {} e o {} jogou {}".format(computer_choice, user, move))
                menu()
            elif computer_choice == "Tesoura" and move == "Papel":
                print("O Computador Ganhou\n")
                print("O computador jogou {} e o {} jogou {}".format(computer_choice, user, move))
                menu()
            elif computer_choice == "Papel" and move == "Pedra":
                print("O Computador Ganhou\n")
                print("O computador jogou {} e o {} jogou {}".format(computer_choice, user, move))
                menu()
            else:
                print("Muitos Parabéns, " + str(user))
                print("O computador jogou {} e  o {} jogou {}".format(computer_choice, user, move))
                menu()
        else:
            print("\n Escolha não válida.\n Tente outra vez.")  # invalid choice message

game()  # start the game
