def correct_enter(symbol, field):
    correct_cell = False
    while not correct_cell:
        cell = input(f"Enter the cell number in the field (1 to 9) for {symbol} = ")
        if not cell.isdigit():
            print("Entered not a number")
            continue
        else:
            cell = int(cell)
            if 0 < cell < 10:
                if str(field[cell - 1]) in "XO":
                    print("This cell isn't selectable. Choose another cell")
                    continue
                else:
                    field[cell - 1] = symbol
                    correct_cell = True
            else:
                print("This isn`t a correct cell. ")
