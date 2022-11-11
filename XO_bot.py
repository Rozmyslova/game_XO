import random
from game_field import fill_game_field
from correct_enter import correct_enter
from winner_combination import correct_win
from player_symbol import choice_symbol
from player_symbol import bot_symbol


def turn_bot(game_field, player_sym, bot_sym):
    bot_choice = False
    new_combination = list()
    win_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    while not bot_choice:
        for elements in win_combination:
            if game_field[elements[0]] in [player_sym, bot_sym] and game_field[elements[1]] in [player_sym, bot_sym] \
                    and game_field[elements[2]] in [player_sym, bot_sym]:
                continue
            new_combination.append(elements)
        for elements in new_combination:
            buf = [i for i in elements if game_field[i] == bot_sym]
            if len(buf) == 2:
                game_field[elements[0]] = bot_sym
                game_field[elements[1]] = bot_sym
                game_field[elements[2]] = bot_sym
                return True
        for elements in new_combination:
            buf = [i for i in elements if game_field[i] == player_sym]
            if len(buf) == 2:
                for i in elements:
                    if game_field[i] != player_sym:
                        game_field[i] = bot_sym
                        return True
        not_used_cells = [i for i in game_field if i not in [player_sym, bot_sym]]
        cell = random.choice(not_used_cells)
        game_field[cell - 1] = bot_sym
        return False


def game_bot():
    player_symbol = choice_symbol()
    correct_sym = False
    while not correct_sym:
        bot_symbol_ch = random.randint(1, 9)
        bot_sym = bot_symbol(bot_symbol_ch)
        if bot_sym == player_symbol:
            print("This symbol isn`t available. Choose another one ")
            continue
        else:
            correct_sym = True
    field = list(range(1, 10))
    fill_game_field(field)
    turn = 1
    while turn < 10:
        if turn % 2 != 0:
            print("Player's turn")
            player = "Player"
            correct_enter(player_symbol, field)
            fill_game_field(field)
        else:
            print("Bot's turn")
            player = "Bot"
            turn_bot(field, player_symbol, bot_sym)
            fill_game_field(field)
        if turn > 4:
            if correct_win(field):
                print(f"{player} is winner")
                break
            elif turn == 9:
                print("Friendship won")
        turn += 1
