from PyQt5.QtWidgets import QDialog, QVBoxLayout,QPushButton, QComboBox, QLabel

class PlayerDialog(QDialog):
    def __init__(self, available_players, parent=None):
        super(PlayerDialog, self).__init__(parent)
        layout = QVBoxLayout(self)

        self.label = QLabel("Choose who you want to randomly draw from:")
        layout.addWidget(self.label)

        self.players_combobox = QComboBox()
        for choosable_player in available_players:
            self.players_combobox.addItem(str(choosable_player))
        layout.addWidget(self.players_combobox)

        self.button2 = QPushButton("draw !")
        self.button2.clicked.connect(self.select_player)
        layout.addWidget(self.button2)


    def select_player(self):
        self.selected_player = self.players_combobox.currentText()
        self.accept()

    def get_selected_player(self):
        return self.selected_player