import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QGridLayout, QSpacerItem, QGroupBox, QWidgetItem
from PyQt5.QtGui import QPalette, QColor,QFont

from random import randint, choice

CARDS = ['0','1','2','3','4','5','6','7','8','9','+','-','x']

class Card_Button(QPushButton):
    def __init__(self, button_text, parent=None):
        super(Card_Button, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)
        self.toggled.connect(self.on_toggled)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Set size policy
        self.update_button()
        self.setText(button_text)

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
    def __init__(self):
        super().__init__()
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setStyleSheet("padding: 0; margin: 0; ")


        button_throw = QPushButton('throw')
        button_pass = QPushButton('pass')
        button_draw = QPushButton('draw')
        button_special_draw = QPushButton('special_draw')
        #spacer_item = QWidgetItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        #self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.buttons = [button_throw, button_pass, button_draw, button_special_draw]

        for button in self.buttons:
            self.widget_layout.addWidget(button)
            #button.setSizePolicy(size_policy)

        #self.widget_layout.addWidget(spacer_item)
        self.setLayout(self.widget_layout)



class Hand_Of_Cards(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(2) # Spacing between cards
        self.widget_layout.setContentsMargins(1, 20, 1, 1) # Marging arround cards
        
        self.buttons = []
        self.cards_value_list = []
        self.setStyleSheet("padding: 0; margin: 0; ")

        rand_c = randint(5,10)

        for card_number in range(rand_c):
            value = choice(CARDS)
            button = Card_Button(value)
            self.cards_value_list.append(value)
            self.buttons.append(button)
            self.widget_layout.addWidget(button) #, 0, card_number)

        self.setMaximumWidth(rand_c*100)

        self.setLayout(self.widget_layout)

    def refresh_cards(self ):
        # To handle diffrently
        self.cards_value_list = ['1','2','+']

        # Flush all buttons
        self.buttons = []

        if self.widget_layout is not None:
            while self.widget_layout.count():
                item = self.widget_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        for index, card in enumerate(self.cards_value_list):
            button = Card_Button(card)
            self.buttons.append(button)
            self.widget_layout.addWidget(button, 0, index)

        self.setMaximumWidth(len(self.cards_value_list)*100)


    def get_button_states(self):
        button_checked = []
        for button in self.buttons:
            if button.isChecked():
                button_checked.append(button.text())
        print(button_checked)


class Make_Move_Interface(QWidget):
    def __init__(self):
        super().__init__()

        # Create a vertical layout
        widget_layout = QVBoxLayout()

        # Create a group box
        groupBox = QGroupBox("Player_name")

        # create bts
        self.hand = Hand_Of_Cards()
        self.action = Action_buttons()

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
        
        ### 1 creer le layout
        self.widget_layout = QVBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        # layout_container = QGridLayout()

        ### 2 creer les wiggets
        self.player1_interface = Make_Move_Interface()
        self.player2_interface = Make_Move_Interface()

        ### 3 ajouter les widget dans le layout (child)
        self.widget_layout.addWidget(self.player1_interface)
        self.widget_layout.addWidget(self.player2_interface)

        ### - resize layout ?
        #layout_size = self.widget_layout.sizeHint()
        #layout_size.setHeight(500)
        #self.setFixedSize(layout_size)

        # widget_b = QWidget()
        # widget_b.setLayout(layout_container)
        # layout_container.addWidget(widget_b, 0, 0)

        ### 4 create container widget
        widget = QWidget()
        widget.setStyleSheet("padding: 0; margin: 0; ")

        ### 5 SET the layout for the Wigget (parent widget)
        widget.setLayout(self.widget_layout)
        self.setCentralWidget(widget)
        self.resize(800, 300) # Ne fait rien


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())