import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from Theta_core import *  # Import your game logic module

class ThetaController:
    def __init__(self):
        self.game = Theta_Game(3)  # Initialize your game

    def distribute_cards(self):
        self.game.distribute()  # Distribute cards

    def player1_throw(self):
        self.game.player_throw(0)  # Perform action for player 1

    def player2_throw(self):
        self.game.player_throw(1)  # Perform action for player 2

class ThetaView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        btn_distribute = QPushButton('Distribute Cards')
        btn_distribute.clicked.connect(self.controller.distribute_cards)
        btn_player1_throw = QPushButton('Player 1 Throw')
        btn_player1_throw.clicked.connect(self.controller.player1_throw)
        btn_player2_throw = QPushButton('Player 2 Throw')
        btn_player2_throw.clicked.connect(self.controller.player2_throw)

        layout.addWidget(btn_distribute)
        layout.addWidget(btn_player1_throw)
        layout.addWidget(btn_player2_throw)

        self.setLayout(layout)

class ThetaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Theta Game")
        self.controller = ThetaController()
        self.view = ThetaView(self.controller)
        self.setCentralWidget(self.view)

def main():
    app = QApplication(sys.argv)
    window = ThetaApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
