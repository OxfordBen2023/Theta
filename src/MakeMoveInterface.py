from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel
from PyQt5.QtGui import QPixmap
from src.ActionButtons import ActionButtons
from src.HandOfCards import HandOfCards


class MakeMoveInterface(QWidget):
    def __init__(self, player_index, player_name, player_icon):
        super().__init__()

        self.player_number = player_index
        self.player_name = player_name
        self.player_icon = player_icon

        # Create a horizontal layout
        widget_layout = QHBoxLayout()

        # Create a group box
        groupBox = QGroupBox(self.player_name)

        # Create a QLabel to display the image
        self.image_label = QLabel()
        self.load_image(f"resources/players_img/perso{str(self.player_icon).zfill(2)}.png")
        self.image_label.setMaximumSize(100, 100)
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
        widget_layout.addWidget(self.image_label)
        widget_layout.addWidget(groupBox)

        self.setGeometry(300, 300, 300, 200)
        self.setLayout(widget_layout)
    
    
    def load_image(self, image_path):
        # Load the image from the specified path
        pixmap = QPixmap(image_path)

        # Set the pixmap to the QLabel to display the image
        self.image_label.setPixmap(pixmap.scaled(100, 100))