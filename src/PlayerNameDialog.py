from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QDialog, QLineEdit


class PlayerNameDialog(QDialog):
    def __init__(self, player_number, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Names")

        # Create Layout
        self.layout = QVBoxLayout()

        # Create Labels and LineEdits for player names
        self.player_name_labels = []
        self.player_name_edits = []

        for i in range(player_number): 
            label = QLabel(f"Player {i+1}:", self)
            edit = QLineEdit(self)
            self.layout.addWidget(label)
            self.layout.addWidget(edit)
            self.player_name_labels.append(label)
            self.player_name_edits.append(edit)

        # Create OK and Cancel Buttons
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # Add Buttons to Layout
        self.layout.addWidget(self.ok_button)
        self.layout.addWidget(self.cancel_button)

        self.setLayout(self.layout)

    def get_player_dict(self):
        player_dict = {}
        for index, line_edit in enumerate(self.player_name_edits):
            if not line_edit.text():
                print("At least one player has no name.")
                return None
            else:
                player_dict[index] = line_edit.text()
        return player_dict