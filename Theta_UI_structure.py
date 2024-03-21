import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QGridLayout, QSpacerItem, QGroupBox, QWidgetItem
from PyQt5.QtGui import QPalette, QColor,QFont

from random import randint, choice

from Theta_core import *


# CARDS = ['0','1','2','3','4','5','6','7','8','9','+','-','x']

# GAME = Theta_Game(3)
# GAME.distribute()
# print(f'ref: {GAME.player_list[0].cards}')


class Card_Button(QPushButton):
    def __init__(self, button_text, parent=None):
        super(Card_Button, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)
        self.toggled.connect(self.on_toggled)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Set size policy
        self.update_button()
        self.setText(str(button_text))

        font = QFont()
        font.setPointSize(20)  # Set font size to 16 points
        self.setFont(font)

    def on_toggled(self):
        self.update_button()

    def update_button(self):
        if self.isChecked():
            self.setStyleSheet("background-color: green; color: white;")
        else:
            self.setStyleSheet("background-color: red; color: white; ")


class Action_buttons(QWidget):
    ### The hand instance is passed so it can be refreshed.
    def __init__(self, hand_instance):
        super().__init__()
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.hand = hand_instance
        
        self.setStyleSheet("padding: 0; margin: 0; ")


        self.button_throw = QPushButton('throw')
        self.button_pass = QPushButton('pass')
        self.button_draw = QPushButton('draw')
        self.button_special = QPushButton('special_draw')

        #spacer_item = QWidgetItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        #self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.buttons = [self.button_throw, 
                        self.button_pass, 
                        self.button_draw, 
                        self.button_special]

        for button in self.buttons:
            self.widget_layout.addWidget(button)
            #button.setSizePolicy(size_policy)

        #self.widget_layout.addWidget(spacer_item)
        self.setLayout(self.widget_layout)


class Hand_Of_Cards(QWidget):
    def __init__(self, player_cards):
        super().__init__()
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(2) # Spacing between cards
        self.widget_layout.setContentsMargins(1, 20, 1, 1) # Marging arround cards
        
        self.buttons = []
        self.cards_value_list = player_cards
        self.setStyleSheet("padding: 0; margin: 0; ")


        for card_value in self.cards_value_list:
            button = Card_Button(card_value)
            self.buttons.append(button)
            self.widget_layout.addWidget(button) #, 0, card_number)

        self.setMaximumWidth(len(self.cards_value_list)*100)
        self.setLayout(self.widget_layout)

    def refresh_cards(self, player_cards):

        self.cards_value_list = player_cards

        # Flush all buttons
        self.buttons = []

        # flush previous cards
        if self.widget_layout is not None:
            while self.widget_layout.count():
                item = self.widget_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        # redraw all cards
        for card_value in self.cards_value_list:
            button = Card_Button(card_value)
            self.buttons.append(button)
            self.widget_layout.addWidget(button)

        self.setMaximumWidth(len(self.cards_value_list)*100)


    def get_button_states(self):
        button_checked = []
        for button in self.buttons:
            if button.isChecked():
                button_checked.append(button.text())
        return button_checked


class Make_Move_Interface(QWidget):
    def __init__(self, player_index, player_name):
        super().__init__()

        self.player_number = player_index
        self.player_name = player_name

        # Create a vertical layout
        widget_layout = QVBoxLayout()

        # Create a group box
        groupBox = QGroupBox(self.player_name)

        # create bts

        ### Hands of cards gets the cards from the game ('?' Are waiting to be initialised and shouldn't show)
        self.hand = Hand_Of_Cards(['?','?','?','?'])
        ### The hand is given to the Action_buttons method to allow a refresh later.
        self.action = Action_buttons(self.hand)

        # Add buttons to the group box layout
        grp_box_layout = QVBoxLayout()
        grp_box_layout.addWidget(self.hand)
        grp_box_layout.addWidget(self.action)

        # Set the layout of the group box
        groupBox.setLayout(grp_box_layout)

        self.setStyleSheet("padding: 0; margin: 0; ")
        widget_layout.setSpacing(0)
        widget_layout.setContentsMargins(0, 10, 0, 0)
 
        # Add the group box to the main layout

        widget_layout.addWidget(groupBox)

        self.setGeometry(300, 300, 300, 200)


        self.setLayout(widget_layout)



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
            self.interface_player_dict[player_index]= Make_Move_Interface(player_index, player_name)
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




app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())