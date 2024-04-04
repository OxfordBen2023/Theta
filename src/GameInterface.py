from PyQt5.QtWidgets import QWidget, QVBoxLayout
from src.MakeMoveInterface import MakeMoveInterface
from PyQt5.QtCore import pyqtSignal 
from src.utils import *

from src.Theta_core import *


class GameInterface(QWidget):
    game_over_signal = pyqtSignal()
    def __init__(self, player_dict_name, player_dict_icon):
        super().__init__()

        self.player_name_dict = player_dict_name
        self.player_icon_dict = player_dict_icon
        
        self.game = Theta_Game(self.player_name_dict)
        self.game.distribute()

        ### 1 create layout
        self.widget_layout = QVBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        ### 2 create wiggets
        self.interface_player_dict = {}
        for player_index, player_name in self.player_name_dict.items():
            self.interface_player_dict[player_index]= MakeMoveInterface(player_index, player_name, self.player_icon_dict[player_index])
            self.interface_player_dict[player_index].action.button_throw.clicked.connect(self.throw_btn_pressed)
            self.interface_player_dict[player_index].action.button_pass.clicked.connect(self.pass_btn_pressed)
            self.interface_player_dict[player_index].action.button_draw.clicked.connect(self.draw_btn_pressed)
            self.interface_player_dict[player_index].action.button_special.clicked.connect(self.special_btn_pressed)

        ### 3 add widgets inlayout
            self.widget_layout.addWidget(self.interface_player_dict[player_index])


        ### 4 assign layout to self
        self.setLayout(self.widget_layout)

        self.resize(700, 550)
        self.update_all_interface('initialise')

    def throw_btn_pressed(self):
        self.update_all_interface('throw')

    def pass_btn_pressed(self):
        self.update_all_interface('pass')

    def draw_btn_pressed(self):
        self.update_all_interface('draw')

    def special_btn_pressed(self):
        self.update_all_interface('special')

    def update_all_interface(self, action_wanted):
        print('============================')
        current_player = self.game.active_player
        print(f'{self.player_name_dict[current_player]} has just played !')
        print(f"the wanted action is: {action_wanted}")
        selected_cards = self.interface_player_dict[current_player].hand.get_button_states()
        print(f'the selected cards are: {selected_cards}')
        
        if action_wanted is not 'initialise':
            error_message = self.game.play_round(action_wanted,selected_cards)
            if error_message:
                show_message(error_message)

        # refresh cards
        for index, interface in self.interface_player_dict.items():
            if self.game.active_player == index:
                interface.hand.refresh_cards(self.game.player_dict[index].cards, enable = True)
            else:
                interface.hand.refresh_cards(self.game.player_dict[index].cards, enable = False)
                                                     
        # Game Over
        if self.game.game_over():
            game_over_text = self.game.compute_gameover_text()
            show_message(game_over_text)
            self.game_over_signal.emit()


        # active window
        for index, interface in self.interface_player_dict.items():
            if self.game.active_player == index:
                interface.setEnabled(True)
            else:
                interface.setEnabled(False)
