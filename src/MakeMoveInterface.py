from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox
from src.Action_Buttons import ActionButtons
from src.HandOfCards import HandOfCards


class MakeMoveInterface(QWidget):
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
        self.hand = HandOfCards(['?','?','?','?'])
        ### The hand is given to the ActionButtons method to allow a refresh later.
        self.action = ActionButtons(self.hand)

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