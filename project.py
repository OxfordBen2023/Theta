import sys
from PyQt5.QtWidgets import QApplication
from src.MainWindow import MainWindow
import inflect



def create_score_str(cards):
    """
    Create the best mathematical operation from the final cards of the player. 
    In case of an uncorrect mathematical expression ( like 5+6++ ) the rules gives a -5 penality by uncorrect cards.

    exemples: 
    input : ['7','x','2','+','8'] returns " 8 x 7 + 2"
    input : ['7','x','2','+','-'] returns " 7 x 2 [-5][-5]" 
    """

    # Testing the validity of the imput cards:
    if len(cards) != 5:
        raise ValueError("Not the right amount of cards. (ie: Player finished with cards != 5)")
    for card in cards:
        if not card in ['0','1','2','3','4','5','6','7','8','9','+','-','x']:
            raise ValueError("Invalid card detected.")


    # filtering numbers from signs :
    number_list = []
    sign_list = []
    for card in cards:
        if card.isnumeric():
            number_list.append(card)
        else:
            sign_list.append(card)
    # sorting both numbers and signs by level of interest :
    sign_values = {"x": 3, "+": 2, "-": 1} 
    number_list.sort(reverse=True)
    sign_list.sort(key=lambda x: sign_values.get(x, 0), reverse=True)

    # computing score_string :
    can_keep_combining = True
    score_string = ""
    while can_keep_combining:
        if len(number_list)==0:
            can_keep_combining = False
            for _ in range(len(number_list+sign_list)):
                score_string += " [-5]"
        else:
            score_string += f" {number_list[0]}"
            number_list.pop(0)
            if len(sign_list)==0 or len(number_list)==0:
                can_keep_combining = False
                for _ in range(len(number_list+sign_list)):
                    score_string += " [-5]"
            else:
                score_string += f" {sign_list[0]}"
                if sign_list[0] == '-':
                    number_list.sort()  # after a minus sign, we want the smallest number available
                sign_list.pop(0)
    return score_string

def evaluate_score(score_string):
    """
    convert the score string in the corresponding int value
    """
    # evaluate score string
    clean_math = ""
    for char in score_string:
        if not char in ['0','1','2','3','4','5','6','7','8','9','+','-','x'," ", "[", "]"]:
            raise ValueError("Invalid card detected.")
        if char not in [" ", "[", "]"]:
            char = '*' if char=='x' else char
            clean_math += char

    score = eval(clean_math)
    return score

def score_text(input_dict):
    """
    Returns the string for the final dialog window to display all scores and rank the players.
    It also takes care of ex aequo. 
    """
    player_score_dict = {}
    gameover_text = "Here are your scores:\n"

    for player in input_dict.values():
        score_string = create_score_str(player.cards)
        score_int = evaluate_score(score_string)
        player_score_dict[player.name] = [score_string, score_int]
        # gameover_text += f"\n\n{player.name}   {score_string}  =  {score_int}\n\n"

    # Sort by the score_int (which is the second element in the list of values)
    sorted_player = sorted(player_score_dict.items(), key=lambda item: item[1][1], reverse=True)
    # `sorted_player` will be a list of tuples, where each tuple is (player_name, [score_string, score_int])

    p = inflect.engine()
    rank = 1
    stored_score = -100
    while len(sorted_player) > 0:        
        player_name, score = sorted_player[0]
        if not score[1] == stored_score:
            gameover_text += f"\n{p.ordinal(rank)}: \n"
        gameover_text += f"{player_name}   {score[0]}  =  {score[1]}\n"
        stored_score = score[1]
        rank += 1
        sorted_player.pop(0)
    print(gameover_text)
    return gameover_text


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()