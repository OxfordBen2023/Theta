from PyQt5.QtWidgets import QMessageBox
from src.PlayerDialog import PlayerDialog

def show_error_message(text_error):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text_error)
    msg.setWindowTitle("Wrong move")
    msg.exec_()


def show_player_dialog(available_players):
    pld = PlayerDialog(available_players)
    pld.setWindowTitle("choose your player")
    pld.exec_()
    return pld.get_selected_player()
