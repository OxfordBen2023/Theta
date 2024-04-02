from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox
from PyQt5.QtCore import Qt


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
        
        # Add the child Widgets to the layout
        self.widget_layout.addWidget(title_label)
        self.widget_layout.addWidget(instructions_label)
        self.widget_layout.addWidget(self.player_combo_box)
        self.widget_layout.addWidget(self.button_start)

        # Set the layout to the current Widget
        self.setLayout(self.widget_layout)

