from PyQt5.QtWidgets import QMessageBox
from src.PlayerChooseDialog import PlayerChooseDialog
from src.PlayerNameDialog import PlayerNameDialog


def show_message(text_error):
    msg = QMessageBox()
    if "finished playing" in text_error:
        msg.setIcon(QMessageBox.Information)
        msg.setText(text_error)
        msg.setWindowTitle("Player out")
    elif "Here are your scores" in text_error:
        msg.setIcon(QMessageBox.Information)
        msg.setText(text_error)
        msg.setWindowTitle("Game over")  
    else:
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text_error)
        msg.setWindowTitle("Wrong move")        
    msg.exec_()

def show_choose_player_dialog(available_players):
    pld = PlayerChooseDialog(available_players)
    pld.setWindowTitle("choose your player")
    pld.exec_()
    return pld.get_selected_player()


def show_name_player_dialog(player_number):
    pld = PlayerNameDialog(player_number)
    pld.exec_()
    if pld.cancel == True:
        return None, None
    else:
        return pld.get_player_dict()
