from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtGui import QFont


class CardButton(QPushButton):
    def __init__(self, button_text, parent=None):
        super(CardButton, self).__init__(parent)
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