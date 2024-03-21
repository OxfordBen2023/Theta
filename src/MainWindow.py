from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from src.MakeMoveInterface import MakeMoveInterface

from src.Theta_core import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Theta game")
        self.setStyleSheet("padding: 0; margin: 0; ")

        self.player_name_dict = {0:'player_1', 
                                 1:'player_2',
                                 2:'player_3'}
        
        self.game = Theta_Game(self.player_name_dict)
        self.game.distribute()
        
        ### 1 create layout
        self.widget_layout = QVBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        ### 2 create wiggets
        self.interface_player_dict = {}  # utile?
        for player_index, player_name in self.player_name_dict.items():
            self.interface_player_dict[player_index]= MakeMoveInterface(player_index, player_name)
            self.interface_player_dict[player_index].action.button_throw.clicked.connect(self.throw_btn_pressed)
            self.interface_player_dict[player_index].action.button_pass.clicked.connect(self.pass_btn_pressed)
            self.interface_player_dict[player_index].action.button_draw.clicked.connect(self.draw_btn_pressed)
            self.interface_player_dict[player_index].action.button_special.clicked.connect(self.special_btn_pressed)

        ### 3 add widgets inlayout
            self.widget_layout.addWidget(self.interface_player_dict[player_index])

        ### 4 create container widget
        widget = QWidget()
        widget.setStyleSheet("padding: 0; margin: 0; ")

        ### 5 set the layout for the Wigget (parent widget)
        widget.setLayout(self.widget_layout)
        self.setCentralWidget(widget)
        self.resize(800, 300) # Does not work ??

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
            print("GAME WILL DO BUISNESS")
            self.game.next_player()


        # refresh cards
        for index, interface in self.interface_player_dict.items():
            interface.hand.refresh_cards(self.game.player_dict[index].cards)
        
        # active window
        for index, interface in self.interface_player_dict.items():
            if self.game.active_player == index:
                interface.setEnabled(True)
            else:
                interface.setEnabled(False)