from random import randint
from src.utils import *
#from src.PlayerDialog import PlayerDialog

#import os

ALL_THETA_CARDS = [0,9,1,1,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,
        '+','+','+','+','+','+','+','+','+','+','-','-','-','-','-','-','-','-','x','x','x','x','x','x']

# convert all to string to avoid future type conflict:
for index, item in enumerate(ALL_THETA_CARDS):
    if type(item) == int:
        ALL_THETA_CARDS[index] = str(item)

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

    def play_round(self, action, selected_cards):
        selected_nbr = len(selected_cards)
        next_player = self.active_player+1
        if next_player > self.player_nbr-1:
            next_player = 0

        if action == 'throw':
            if selected_nbr < 2 or selected_nbr > 4:
                # returns error message if the move is not good
                return "You need to select a number of cards between 2 and 4 for this move."
            my_rand = randint(0, selected_nbr-1)
            selected_cards.pop(my_rand)
            for card_to_remove in selected_cards:
                self.player_dict[self.active_player].cards.remove(card_to_remove)
                self.draw_pile.append(card_to_remove)

        if action == 'pass':
            if selected_nbr < 2 or selected_nbr > 4:
                # returns error message if the move is not good
                return "You need to select a number of cards between 2 and 4 for this move."
            my_rand = randint(0, selected_nbr-1)
            selected_cards.pop(my_rand)
            for card_to_transfer in selected_cards:
                self.player_dict[next_player].cards.append(card_to_transfer)
                self.player_dict[self.active_player].cards.remove(card_to_transfer)

        if action == 'draw':
            if not self.draw_pile:
                # returns error message if the move is not good
                return "There is no more card to draw, the pile is empty. Choose another action"
            my_rand = randint(0, len(self.draw_pile)-1)
            self.player_dict[self.active_player].cards.append(self.draw_pile[my_rand])
            self.draw_pile.pop(my_rand)

        if action == 'special':
            if selected_nbr != 2 or selected_cards[0] != selected_cards[1]:
                # returns error message if the move is not good
                return "You need to select two identical cards to make a special draw"

            # Send the unwanted cards to the draw pile.
            for card_to_remove in selected_cards:
                self.player_dict[self.active_player].cards.remove(card_to_remove)
                self.draw_pile.append(card_to_remove)

            available_player = []
            for player_index, player in self.player_dict.items():
                if player_index != self.active_player:
                    available_player.append(player.name)
            
            chosen_player = show_player_dialog(available_player)

            # Get chosen player index from the dict :
            for index, name in self.name_dict.items():
                if name == chosen_player:
                    chosen_player_index = index

            # Random car exchange from chosenplayer to curent player
            my_rand = randint(0, len(self.player_dict[chosen_player_index].cards)-1)
            print(f"The randomly selected card is : {self.player_dict[chosen_player_index].cards[my_rand]}")
            self.player_dict[self.active_player].cards.append(self.player_dict[chosen_player_index].cards[my_rand])
            self.player_dict[chosen_player_index].cards.pop(my_rand)


        self.next_player()
        return None





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


