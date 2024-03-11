from random import randint


#import os

my_list = [0,9,1,1,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,
        '+','+','+','+','+','+','+','+','+','+','-','-','-','-','-','-','-','-','x','x','x','x','x','x']
pioche = []

 
class Teta_game:
    def __init__(self, player_nbr):
        self.player_nbr = player_nbr
        self.player_list = []
        for x in range(player_nbr):
            self.player_list.append(Player(x))

    def distribute(self):
        while len(my_list)-60 + 10 * self.player_nbr > 0:
            for player in self.player_list:
                myrand = randint(0,len(my_list)-1)
                player.cards.append(my_list[myrand])
                my_list.pop(myrand)

class Player:
    def __init__(self,id):
        self.id = id
        self.cards = []

    def defausse(self, cards_to_defausse):
        cards_to_defausse.sort(reverse=True)
        myrand = randint(0,len(cards_to_defausse)-1)
        for df_card in cards_to_defausse:
            if not df_card == myrand:
                to_pioche = self.cards.pop(df_card)
                pioche.append(to_pioche)
                

    


game = Teta_game(3)
game.distribute()

print(game.player_list[0].cards)
game.player_list[0].defausse([0,1,2,3])

print(game.player_list[0].cards)
print(f'la pioche : {pioche}')

