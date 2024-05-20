from PyQt5.QtWidgets import QDialog, QVBoxLayout,QPushButton, QComboBox, QLabel

# Just to remove this warning when toggling the combobox: qt.qpa.wayland: Wayland does not support QWindow::requestActivate()
import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.wayland.warning=false"

class PlayerChooseDialog(QDialog):
    def __init__(self, available_players, parent=None):
        super(PlayerChooseDialog, self).__init__(parent)
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