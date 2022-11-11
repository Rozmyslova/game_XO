import emoji


def choice_symbol():
    print(f"Choose your symbol to play:\n\
            1 - {emoji.emojize(':bear:')} - bear;\n\
            2 - {emoji.emojize(':bell:')} - bell;\n\
            3 - {emoji.emojize(':black_heart:')} - black heart;\n\
            4 - {emoji.emojize(':blue_heart:')} - blue heart;\n\
            5 - {emoji.emojize(':boy_light_skin_tone:')} - boy;\n\
            6 - {emoji.emojize(':cat_face:')} - cat;\n\
            7 - {emoji.emojize(':girl:')} - girl;\n\
            8 - {emoji.emojize(':fire:')} - fire;\n\
            9 - {emoji.emojize(':red_heart:')} - red_heart")
    choice = input("Choose the number of the symbol: ")
    if choice == '1':
        symbol = emoji.emojize(':bear:')
    elif choice == '2':
        symbol = emoji.emojize(':bell:')
    elif choice == '3':
        symbol = emoji.emojize(':black_heart:')
    elif choice == '4':
        symbol = emoji.emojize(':blue_heart:')
    elif choice == '5':
        symbol = emoji.emojize(':boy_light_skin_tone:')
    elif choice == '6':
        symbol = emoji.emojize(':cat_face:')
    elif choice == '7':
        symbol = emoji.emojize(':girl:')
    elif choice == '8':
        symbol = emoji.emojize(':fire:')
    elif choice == '9':
        symbol = emoji.emojize(':red_heart:')
    else:
        print("No such a symbol")
    return symbol


def bot_symbol(choice):
    if choice == '1':
        symbol = emoji.emojize(':bear:')
    elif choice == '2':
        symbol = emoji.emojize(':bell:')
    elif choice == '3':
        symbol = emoji.emojize(':black_heart:')
    elif choice == '4':
        symbol = emoji.emojize(':blue_heart:')
    elif choice == '5':
        symbol = emoji.emojize(':boy_light_skin_tone:')
    elif choice == '6':
        symbol = emoji.emojize(':cat_face:')
    elif choice == '7':
        symbol = emoji.emojize(':girl:')
    elif choice == '8':
        symbol = emoji.emojize(':fire:')
    else:
        symbol = emoji.emojize(':red_heart:')
    return symbol

