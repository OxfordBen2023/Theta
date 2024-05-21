from PyQt5.QtWidgets import QMainWindow, QWidget,QStackedLayout
from src.utils import *
from src.GameInterface import GameInterface
from src.WelcomScreen import WelcomeScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Theta game")
        self.setStyleSheet("padding: 0; margin: 0; ")
        
        self.stacklayout = QStackedLayout()

        self.welcome_widget = WelcomeScreen()
        self.welcome_widget.button_start.clicked.connect(self.activate_game)
        self.game_interface = GameInterface({0:'placeholder'},{0:'placeholder'})
        self.game_interface.game_over_signal.connect(self.show_title_screen)

        self.stacklayout.addWidget(self.welcome_widget)
        self.stacklayout.addWidget(self.game_interface)

        ### create container widget
        self.widget = QWidget()
        self.widget.setStyleSheet("padding: 0; margin: 0; ")

        ### set the layout for the Wigget (parent widget)
        self.widget.setLayout(self.stacklayout)
        self.setCentralWidget(self.widget)
        self.resize(800, 550)

    def activate_game(self):
        player_nbr = int(self.welcome_widget.player_combo_box.currentText())
        print(player_nbr)
        # call the Window dialog:
        player_dict_name , player_dict_icon = show_name_player_dialog(player_nbr)

        if player_dict_name:
            self.stacklayout.removeWidget(self.game_interface)
            self.game_interface = GameInterface(player_dict_name, player_dict_icon)
            # This not very beatiful ?
            self.game_interface.game_over_signal.connect(self.show_title_screen)

            self.stacklayout.addWidget(self.game_interface)
            self.widget.setLayout(self.stacklayout)
            print(f"count after: {self.stacklayout.count()}")
            self.stacklayout.setCurrentIndex(1)
    
    def show_title_screen(self):
        self.stacklayout.setCurrentWidget(self.welcome_widget)