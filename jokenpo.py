import random
print("\tJOGO DO PAPEL PEDRA TESOURA")
user = str(input("Nome do jogador: "))

def menu():
    opcao = True
    while opcao:
        print("\t\tMenu")
        print("""
            1. Continuar a jogar
            2.Exit/Quit/Saída """)
        opcao = input("Escolha uma opção:  ")
        if opcao == "1":
            jogo()
        elif opcao == "2":
            print("\n Adeus")
            opcao = None
        else:
            print("\n Escolha não válida.\n Tente outra vez.")

def jogo():
    print("\n\n\t\t [1] - Pedra\n\t\t [2] - Tesoura\n\t\t [3] - Papel\n ")
    opcao1 = True
    while opcao1:
        meu = str(input(("Escolha uma opção (escreva a palavra):")))
        mao =meu.lower().capitalize()
        if meu == 'pedra' or meu =='papel' or meu=='tesoura':
            escolha =["Pedra","Tesoura","Papel"]
            cescolha = random.choice(escolha)
            print ("O Computador jogou: ")
            if cescolha == mao:
                print("O computador jogou {} e o {} jogou {}".format(cescolha,user,mao))
                print("Empate")
                menu()
            elif cescolha == "Pedra" and mao == "Tesoura":
                print("O Computador Ganhou\n")
                print("O computador jogou {} e o {} jogou {}".format(cescolha,user,mao))
                menu()
            elif cescolha == "Tesoura" and mao == "Papel":
                print("O Computador Ganhou\n")
                print("O computador jogou {} e o {} jogou {}".format(cescolha,user,mao))
                menu()
            elif cescolha == "Papel" and mao == "Pedra":
                print("O Computador Ganhou\n")
                print("O computador jogou {} e o {} jogouu {}".format(cescolha,user,mao))
                menu()
            else:
                print("Muitos Parabéns,"+str(user))
                print("O computador jogou {} e  o {} jogou {}".format(cescolha,user,mao))
                menu()
        else:
            print("\n Escolha não válida.\n Tente outra vez.")
jogo()
