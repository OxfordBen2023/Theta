from random import randint
from src.utils import *

ALL_THETA_CARDS = [0,9,1,1,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,
        '+','+','+','+','+','+','+','+','+','+','-','-','-','-','-','-','-','-','x','x','x','x','x','x']

# convert all to string to avoid future type conflict:
for index, item in enumerate(ALL_THETA_CARDS):
    if type(item) == int:
        ALL_THETA_CARDS[index] = str(item)

TOTAL_NUMBER_OF_CARDS = len(ALL_THETA_CARDS)
CARDS_BY_PLAYER_NUMBER = 10


class Player():
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.game_over = False
    
    def create_score(self):
        # filtering
        number_list = []
        sign_list = []
        for card in self.cards:
            if card.isnumeric():
                number_list.append(card)
            else:
                sign_list.append(card)
        # sorting
        sign_values = {"x": 3, "+": 2, "-": 1} 
        number_list.sort(reverse=True)
        sign_list.sort(key=lambda x: sign_values.get(x, 0), reverse=True)

        # computing score
        can_keep_combining = True
        score_string = ""
        while can_keep_combining:
            if len(number_list)==0:
                can_keep_combining = False
                for _ in range(len(number_list+sign_list)):
                    score_string += " [-5]"
            else:
                score_string += f" {number_list[0]}"
                number_list.pop(0)
                if len(sign_list)==0 or len(number_list)==0:
                    can_keep_combining = False
                    for _ in range(len(number_list+sign_list)):
                        score_string += " [-5]"
                else:
                    score_string += f" {sign_list[0]}"
                    if sign_list[0] == '-':
                        number_list.sort()  # after a minus sign, we want the smallest number available
                    sign_list.pop(0)

        # evaluate score string
        clean_math = ""
        for char in score_string:
            if char not in [" ", "[", "]"]:
                char = '*' if char=='x' else char
                clean_math += char

        score = eval(clean_math)
        score_string += f" = {score}"         

        return score_string


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
    
    # Set the new active_player at the end of a round.
    def next_player(self):
        self.active_player += 1
        if self.active_player > self.player_nbr-1:
            self.active_player = 0
        
        # Check if everyone is finished, and ends the game.
        if self.game_over():
            return False

        # test if the next player is not already gameover, and moves to the next available player.    
        while self.player_dict[self.active_player].game_over:
            self.active_player += 1
            if self.active_player > self.player_nbr-1:
                self.active_player = 0
    
    # Test if the player has reach the 5 cards limit and set him game_over
    def is_player_game_over(self, player):
        if len(player.cards) == 5:
            player.game_over = True
            return True
        elif len(player.cards) > 5:
            return False
        else:
            show_message('Something is wrong: number of card < 5')

    def game_over(self):
        trigger = True
        for player in self.player_dict.values():
            if len(player.cards) != 5:
                trigger = False       
        return trigger

    def compute_gameover_text(self):
        gameover_text = "Here are your scores : \n\n"
        for player in self.player_dict.values():
            gameover_text += f"{player.name}:\n"
            gameover_text += player.create_score()
            gameover_text += "\n\n"
        return gameover_text

    def play_round(self, action, selected_cards):
        selected_nbr = len(selected_cards)

        next_player = self.active_player+1
        if next_player > self.player_nbr-1:
            next_player = 0
        # test if the next player is not already gameover, and moves to the next available player.    
        while self.player_dict[next_player].game_over:
            next_player += 1
            if next_player > self.player_nbr-1:
                next_player = 0

        available_player = []
        for player_index, player in self.player_dict.items():
            if player_index != self.active_player and player.game_over != True:
                available_player.append(player.name)

        if action == 'throw':
            if selected_nbr < 2 or selected_nbr > 3:
                # returns error message if the move is not good
                return "You need to select a number of cards between 2 and 3 for this move."
            my_rand = randint(0, selected_nbr-1)
            print(f"You keep : {selected_cards[my_rand]}")
            selected_cards.pop(my_rand)
            for card_to_remove in selected_cards:
                self.player_dict[self.active_player].cards.remove(card_to_remove)
                self.draw_pile.append(card_to_remove)
                # gamover check:
                if self.is_player_game_over(self.player_dict[self.active_player]):
                    self.next_player()
                    return " You have finished playing ! "

        if action == 'pass':
            if selected_nbr < 2 or selected_nbr > 4:
                # returns error message if the move is not good
                return "You need to select a number of cards between 2 and 4 for this move."
            if not available_player:
                # returns error message if the move is not good
                return "You are the last player, you can not do this move !"

            my_rand = randint(0, selected_nbr-1)
            print(f"You keep : {selected_cards[my_rand]}")
            selected_cards.pop(my_rand)
            for card_to_transfer in selected_cards:
                self.player_dict[next_player].cards.append(card_to_transfer)
                self.player_dict[self.active_player].cards.remove(card_to_transfer)
                # gamover check:
                if self.is_player_game_over(self.player_dict[self.active_player]):
                    self.next_player()
                    return " You have finished playing ! "

        if action == 'draw':
            if not self.draw_pile:
                # returns error message if the move is not good
                return "There is no more card to draw, the pile is empty. Choose another action"
            if not available_player:
                # returns error message if the move is not good
                return "You are the last player, you can not do this move !"
            my_rand = randint(0, len(self.draw_pile)-1)
            self.player_dict[self.active_player].cards.append(self.draw_pile[my_rand])
            picked_card = self.draw_pile[my_rand]
            print(f"You piked a : {picked_card}")
            self.draw_pile.pop(my_rand)

            # If it is a number draw again.
            if picked_card.isdigit():
                my_rand = randint(0, len(self.draw_pile)-1)
                self.player_dict[self.active_player].cards.append(self.draw_pile[my_rand])
                picked_card = self.draw_pile[my_rand]
                print(f"You piked next : {picked_card}")
                self.draw_pile.pop(my_rand)


        if action == 'special':
            if selected_nbr < 2 or len(set(selected_cards)) != 1:
                # returns error message if the move is not good
                return "You need to select two or more identical cards to make a special draw"
            
            if not available_player:
                # returns error message if the move is not good
                return "You are the last player, you can not do this move !"

            # Ask the user to choose from who he wants to take
            chosen_player = show_choose_player_dialog(available_player)

            # Get chosen player index from the dict :
            for index, name in self.name_dict.items():
                if name == chosen_player:
                    chosen_player_index = index

            # Send ONE unwanted cards to the draw pile. Then loop over the remaining ones to make sure we don't miss a gameover in chosen_player.
            self.player_dict[self.active_player].cards.remove(selected_cards[0])
            self.draw_pile.append(selected_cards[0])
            selected_cards.pop(0)
            for card_to_remove in selected_cards:
                self.player_dict[self.active_player].cards.remove(card_to_remove)
                self.draw_pile.append(card_to_remove)

                # Random card exchange from chosen player to curent player
                my_rand = randint(0, len(self.player_dict[chosen_player_index].cards)-1)
                print(f"The randomly selected card is : {self.player_dict[chosen_player_index].cards[my_rand]}")
                self.player_dict[self.active_player].cards.append(self.player_dict[chosen_player_index].cards[my_rand])
                self.player_dict[chosen_player_index].cards.pop(my_rand)
                # gamover check on chosen player:
                if self.is_player_game_over(self.player_dict[chosen_player_index]):
                    self.next_player()
                    return f"{self.player_dict[chosen_player_index].name} has finished playing ! "
            # gamover check on self:
            if self.is_player_game_over(self.player_dict[self.active_player]):
                self.next_player()
                return "you have finished playing ! "


        self.next_player()
        return None