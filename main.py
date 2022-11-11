from XO_people import game_people
from XO_bot import game_bot


print("Let's start a game! Would you like to play:\n\
        1 - with a bot;\n\
        2 - with another player")
choice = input("Choose the number of the desired action: ")
if choice == '1':
    game_bot()
else:
    game_people()
