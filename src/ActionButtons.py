from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

class ActionButtons(QWidget):
    ### The hand instance is passed so it can be refreshed.
    def __init__(self, hand_instance):
        super().__init__()
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.hand = hand_instance
        
        self.setStyleSheet("padding: 0; margin: 0; ")

        self.button_throw = QPushButton('throw')
        self.button_pass = QPushButton('pass')
        self.button_draw = QPushButton('draw')
        self.button_special = QPushButton('special draw')


        self.buttons = [self.button_throw, 
                        self.button_pass, 
                        self.button_draw, 
                        self.button_special]

        for button in self.buttons:
            self.widget_layout.addWidget(button)

        self.setLayout(self.widget_layout)