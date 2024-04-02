from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QDialog, QLineEdit
from PyQt5.QtCore import Qt

class PlayerNameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Enter Player Names")

        # Create Layout
        self.layout = QVBoxLayout()

        # Create Labels and LineEdits for player names
        self.player_name_labels = []
        self.player_name_edits = []

        for i in range(5):  # Assuming maximum 5 players, adjust as needed
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


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        # Create Layout and style.
        self.widget_layout = QVBoxLayout()
        self.widget_layout.setAlignment(Qt.AlignCenter)

        # Create the child widgets.
        title_label = QLabel("THETA", self)
        title_label.setStyleSheet("font-size: 50px; font-weight: bold; color: #2ecc71;")

        instructions_label = QLabel("Choose your number of players:", self)
        instructions_label.setStyleSheet("color: #34495e;")

        self.player_combo_box = QComboBox(self)
        self.player_combo_box.addItems(["2", "3", "4", "5"])

        self.button_start = QPushButton('Start a new game !')
        self.button_start.setStyleSheet("background-color: #3498db; color: white; padding: 10px 20px; border-radius: 5px;")
        self.button_start.clicked.connect(self.show_player_name_dialog)

        # Add the child Widgets to the layout
        self.widget_layout.addWidget(title_label)
        self.widget_layout.addWidget(instructions_label)
        self.widget_layout.addWidget(self.player_combo_box)
        self.widget_layout.addWidget(self.button_start)

        # Set the layout to the current Widget
        self.setLayout(self.widget_layout)

    def show_player_name_dialog(self):
        dialog = PlayerNameDialog(self)
        if dialog.exec_():
            # Process player names
            player_names = [edit.text() for edit in dialog.player_name_edits]
            # Do something with player names, e.g., start the game with these names
            print("Player Names:", player_names)
