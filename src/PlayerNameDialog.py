from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QGroupBox, QPushButton, QLabel, QDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from random import randint

CUSTUM_USER_ICON_TO_USER = [[2,'Laurent'], [3,'Lucie'], [5,"Edgar"], [22,"Gustave"], [28,"Léa"], [18,"Louis"]]

class IconButton(QPushButton):
    def __init__(self, index, parent=None):
        super(IconButton, self).__init__(parent)

        self.index = index
        self.clicked.connect(self.update_button)
        self.update_button()
        self.icon = QIcon(f"resources/players_img/perso{str(self.index).zfill(2)}.png")
        self.setIcon(self.icon)

        size = self.icon.actualSize(QSize(150, 150))  # Set the size of the icon as required
        self.setIconSize(size)

    def refresh(self):
        self.icon = QIcon(f"resources/players_img/perso{str(self.index).zfill(2)}.png")
        self.setIcon(self.icon)

    def update_button(self):
        self.index +=1
        if self.index > 28:
            self.index = 1
        self.refresh()


class PlayerNameDialog(QDialog):
    def __init__(self, player_number, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Name your players")

        self.cancel = False

        # Create Layout
        self.layout = QGridLayout()

        # Create groupbox and LineEdits for player names
        self.player_name_edits = []
        self.player_icon_button_list = []

        for i in range(player_number): 

        # Create a group box
            groupBox = QGroupBox(f"Player {i+1}:", self)
            grp_box_layout = QVBoxLayout()
            groupBox.setLayout(grp_box_layout)

            icon_number = randint(1,28)
                    
            edit = QLineEdit(self)
            icon_button = IconButton(icon_number)

            grp_box_layout.addWidget(edit)
            grp_box_layout.addWidget(icon_button)

            self.layout.addWidget(groupBox, i//3, i%3)

            self.player_name_edits.append(edit)
            self.player_icon_button_list.append(icon_button)

        # Create OK Button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)


        # Add Buttons to Layout
        self.layout.addWidget(self.ok_button, 3, 1 if player_number==2 else 2)

        self.setLayout(self.layout)
        self.pre_fill_function()

    def closeEvent(self, event):
        self.cancel = True
        event.accept()


    def get_player_dict(self):
        player_dict = {}
        player_icon_dict = {}
        for index, line_edit in enumerate(self.player_name_edits):
            if not line_edit.text():
                print("At least one player has no name.")
                return None, None
            else:
                player_dict[index] = line_edit.text()
                player_icon_dict[index] = self.player_icon_button_list[index].index

        return player_dict, player_icon_dict
    
    def pre_fill_function(self):
        
        # Random players choice from the custom list
        used_vales = []
        for index, button in enumerate(self.player_icon_button_list):
            random_index = randint(0, len(CUSTUM_USER_ICON_TO_USER)-1)
            while random_index in used_vales:
                random_index = randint(0, len(CUSTUM_USER_ICON_TO_USER)-1)
            used_vales.append(random_index)
            button.index = CUSTUM_USER_ICON_TO_USER[random_index][0]
            self.player_name_edits[index].setText(CUSTUM_USER_ICON_TO_USER[random_index][1])
            button.refresh()