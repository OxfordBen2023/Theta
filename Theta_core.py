from random import randint


#import os

ALL_THETA_CARDS = [0,9,1,1,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,
        '+','+','+','+','+','+','+','+','+','+','-','-','-','-','-','-','-','-','x','x','x','x','x','x']
TOTAL_NUMBER_OF_CARDS = len(ALL_THETA_CARDS)
CARDS_BY_PLAYER_NUMBER =10
 
class Theta_Game():
    def __init__(self, name_dict):
        self.player_nbr = len(name_dict)
        self.name_dict = name_dict
        self.player_dict = {}
        self.draw_pile = ALL_THETA_CARDS.copy()
        self.active_player = 0
        for index, name in self.name_dict.items():
            self.player_dict[index]= Player(name)

    def distribute(self):
        self.draw_pile = ALL_THETA_CARDS.copy()
        while len(self.draw_pile)-TOTAL_NUMBER_OF_CARDS + CARDS_BY_PLAYER_NUMBER * self.player_nbr > 0:
            for player in self.player_dict.values():
                myrand = randint(0,len(self.draw_pile)-1)
                player.cards.append(self.draw_pile[myrand])
                self.draw_pile.pop(myrand)
    
    def next_player(self):
        self.active_player += 1
        if self.active_player > self.player_nbr-1:
            self.active_player = 0

class Player():
    def __init__(self,name):
        self.name = name
        self.cards = []



                

# dict = {0:'player_1',
#         1:'player_2',
#         2:'player_3'}

# game = Theta_Game(dict)
# print(game.name_dict)

# game.distribute()
# print(game.player_dict[0].cards)
# print(game.player_dict[0].id)


