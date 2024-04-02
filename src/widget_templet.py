from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

class WidgetTemplate(QWidget):
    def __init__(self):
        super().__init__()

        # 1 Create Layout and style.
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setStyleSheet("padding: 0; margin: 0; ")

        # 2 Create the child widgets.

        self.button_1 = QPushButton('one')
        self.button_2 = QPushButton('two')
        self.button_3 = QPushButton('tree')
        self.button_4 = QPushButton('four')

        # 3 Add the child Widgets to the layout
        self.buttons = [self.button_1, 
                        self.button_2, 
                        self.button_3, 
                        self.button_4]

        for button in self.buttons:
            self.widget_layout.addWidget(button)
        
        # 4 Set the layout to the current Widget
        self.setLayout(self.widget_layout)