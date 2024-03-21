from PyQt5.QtWidgets import QWidget, QHBoxLayout
from src.CardButton import CardButton


class HandOfCards(QWidget):
    def __init__(self, player_cards):
        super().__init__()
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setSpacing(2) # Spacing between cards
        self.widget_layout.setContentsMargins(1, 20, 1, 1) # Marging arround cards
        
        self.buttons = []
        self.cards_value_list = player_cards
        self.setStyleSheet("padding: 0; margin: 0; ")

        for card_value in self.cards_value_list:
            button = CardButton(card_value)
            self.buttons.append(button)
            self.widget_layout.addWidget(button) #, 0, card_number)

        self.setMaximumWidth(len(self.cards_value_list)*100)
        self.setLayout(self.widget_layout)

    def refresh_cards(self, player_cards):

        self.cards_value_list = player_cards

        # Flush all buttons
        self.buttons = []

        # flush previous cards
        if self.widget_layout is not None:
            while self.widget_layout.count():
                item = self.widget_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        # redraw all cards
        for card_value in self.cards_value_list:
            button = CardButton(card_value)
            self.buttons.append(button)
            self.widget_layout.addWidget(button)

        self.setMaximumWidth(len(self.cards_value_list)*100)


    def get_button_states(self):
        button_checked = []
        for button in self.buttons:
            if button.isChecked():
                button_checked.append(button.text())
        return button_checked
