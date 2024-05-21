import pytest
from src.Theta_core import Player
from project import create_score_str, evaluate_score, score_text

def test_create_score_str():
    assert create_score_str(['7','x','2','+','8']) == " 8 x 7 + 2"
    assert create_score_str(['0','+','4','-','5']) == " 5 + 4 - 0"
    assert create_score_str(['7','-','2','0','9']) == " 9 - 0 [-5] [-5]"
    assert create_score_str(['7','x','2','+','-']) == " 7 x 2 [-5] [-5]"
    assert create_score_str(['+','x','x','+','-']) == " [-5] [-5] [-5] [-5] [-5]"
    assert create_score_str(['7','7','7','7','7']) == " 7 [-5] [-5] [-5] [-5]"
    with pytest.raises(ValueError):
        create_score_str(['7','x',2,'+','8'])
    with pytest.raises(ValueError):
        create_score_str(['7','x','2','+','8','9'])
    with pytest.raises(ValueError):
        create_score_str(['7','x','2'])

def test_evaluate_score():
    assert evaluate_score(" 8 x 7 + 2") == 58
    assert evaluate_score(" 5 + 4 - 0") == 9
    assert evaluate_score(" 9 - 0 [-5] [-5]") == -1
    assert evaluate_score(" 7 x 2 [-5] [-5]") == 4
    assert evaluate_score(" [-5] [-5] [-5] [-5] [-5]") == -25
    assert evaluate_score(" 7 [-5] [-5] [-5] [-5]") == -13
    with pytest.raises(ValueError):
        create_score_str(['7/0'])
    with pytest.raises(ValueError):
        create_score_str(['cat!'])

def test_score_text():
    player1 = Player('Léa')
    player1.cards = ['4','-','-','2','x']
    player2 = Player('Edgar')
    player2.cards = ['+','0','5','7','x']
    dicttest1 = {1:player1, 2:player2}
    assert score_text(dicttest1) == "Here are your scores:\n\n1st: \nEdgar    7 x 5 + 0  =  35\n\n2nd: \nLéa    4 x 2 [-5] [-5]  =  -2\n"

    # Testing ex aequo on 2nd place
    player3 = Player('Louis')
    player3.cards = ['-','2','x','-','4']
    dicttest2 = {1:player1, 2:player2, 3:player3}
    assert score_text(dicttest2) == "Here are your scores:\n\n1st: \nEdgar    7 x 5 + 0  =  35\n\n2nd: \nLéa    4 x 2 [-5] [-5]  =  -2\nLouis    4 x 2 [-5] [-5]  =  -2\n"

    # Testing ex aequo on 1st place
    player4 = Player('Benoit')
    player4.cards = ['5','x','5','+','6']
    dicttest3 = {1:player1, 2:player2, 3:player4}
    assert score_text(dicttest3) == "Here are your scores:\n\n1st: \nEdgar    7 x 5 + 0  =  35\nBenoit    6 x 5 + 5  =  35\n\n3rd: \nLéa    4 x 2 [-5] [-5]  =  -2\n"

    # testing wrong dictionary
    player5 = Player('Benoit')
    player5.cards = ['1','2','3','4','5','6']
    dicttest4 = {1:player1, 2:player2, 3:player4, 8:player5}
    with pytest.raises(ValueError):
        score_text(dicttest4)
