from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtGui import QFont


class CardButton(QPushButton):
    def __init__(self, button_text, is_enabled=True, parent=None):
        super(CardButton, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)
        self.toggled.connect(self.on_toggled)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Set size policy
        self.is_enabled = is_enabled
        self.update_button()
        self.setText(str(button_text))

        font = QFont()
        font.setPointSize(20)
        self.setFont(font)

    def on_toggled(self):
        self.update_button()


    def update_button(self):
        if not self.is_enabled:
            self.setStyleSheet("background-color: grey; color: white;")

        elif self.isChecked():
            self.setStyleSheet("background-color: green; color: white;")
        else:
            self.setStyleSheet("background-color: red; color: white; ")