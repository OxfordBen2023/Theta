from random import randint
import os

my_list = [0,9,1,1,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,
        '+','+','+','+','+','+','+','+','+','+','-','-','-','-','-','-','-','-','x','x','x','x','x','x']


def teta_game (player_nbr):
    draft_in_a_row = 0
    dist_cards = []
    for x in range(player_nbr): dist_cards.append([])

    def draft(player, card_index):
        next_player = (player+1)%player_nbr
        print("la carte choisie est ----->", dist_cards[player][card_index],'\n')
        dist_cards[next_player].append(dist_cards[player][card_index])
        dist_cards[player].pop(card_index)
    
    def defausse(player, card_index):
        print("la carte choisie est ----->", dist_cards[player][int(card_index)],'\n')
        dist_cards[player].pop(int(card_index))

    def print_game_state():
        print('============THETA=============')
        for player in range(player_nbr):
            print(f"cartes du joueur {player}: (il a {len(dist_cards[player])} cartes en mains)")
            print(dist_cards[player])

    #cards distribution
    while len(my_list)-60 + 10*player_nbr > 0:
        for player in range(player_nbr):
            myrand = randint(0,len(my_list)-1)
            dist_cards[player].append(my_list[myrand])
            my_list.pop(myrand)


    while True:
        for player in range(player_nbr):
            print_game_state()
            print(f"\nLe joueur actif est le numero : {player}")
            print(f"sa main: {dist_cards[player]}")
            dodraft = input("Est ce qu'il draft ? ")
            if dodraft and draft_in_a_row <= (player_nbr-1):
                print("il draft !!")
                card_to_draft = int(input("Quel index de carte il draft de son jeu?\n"))
                draft (player, card_to_draft)
                draft_in_a_row +=1
            else:
                for x in range(3):
                    if draft_in_a_row >= player_nbr-1: 
                        print("limite de draft a la suite atteinte !")
                    draft_in_a_row = 0
                    print("mode defausse")
                    print(f"cartes: {dist_cards[player]}")
                    card_to_def = input("Quel index de carte il defausse?\n")
                    if card_to_def: defausse(player, int(card_to_def))
                    else:
                        print("C'est tout, pas plus de defause." )
                        break
            #Fin de partie
            if len(dist_cards[player])==5:
                print (f'je joueur {player} a finit de jouer !')
                print (f'Voici ces cartes: {dist_cards[player]}')
                dist_cards.pop(player)
                player_nbr -=1
                break
            #os.system('clear')


teta_game(3)



#user_input = input("Que fait le joueur maintenant?\n")
#exec(user_input)

#testt exec() et peut etre eval() pour pouvoir entrer du code