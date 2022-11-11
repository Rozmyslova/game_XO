from game_field import fill_game_field
from correct_enter import correct_enter
from winner_combination import correct_win
from player_symbol import choice_symbol


def game_people():
    print("First player!")
    player_symbol1 = choice_symbol()
    print("Second player!")
    correct_sym = False
    while not correct_sym:
        player_symbol2 = choice_symbol()
        if player_symbol2 == player_symbol1:
            print("This symbol isn`t available. Choose another one ")
            continue
        else:
            correct_sym = True
    field = list(range(1, 10))
    fill_game_field(field)
    turn = 1
    while turn < 10:
        if turn % 2 != 0:
            print("First player's turn")
            player = "First player"
            correct_enter(player_symbol1, field)
            fill_game_field(field)
        else:
            print("Second player's turn")
            player = "Second player"
            correct_enter(player_symbol2, field)
            fill_game_field(field)
        if turn > 4:
            if correct_win(field):
                print(f"{player} is winner")
                break
            elif turn == 9:
                print("Friendship won")
        turn += 1
