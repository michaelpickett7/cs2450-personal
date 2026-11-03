import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show(b):
    for r in range(3):
        print(f" {b[r * 3]} | {b[r * 3 + 1]} | {b[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---")

def winner(box):

    if box[0] == box[1] == box[2]: #win conditions
        return box[0]
    if box[3] == box[4] == box[5]:
        return box[3]
    if box[6] == box[7] == box[8]:
        return box[6]
    if box[0] == box[3] == box[6]:
        return box[0]
    if box[1] == box[4] == box[7]:
        return box[1]
    if box[2] == box[5] == box[8]:
        return box[2]
    if box[0] == box[4] == box[8]:
        return box[0]
    if box[2] == box[4] == box[6]:
        return box[2]
    return None

def play():
    boxes = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in boxes):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(boxes)
        print(f"\n{turn}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and boxes[move].isdigit():
            boxes[move] = turn
            winner_result = winner(boxes)
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(boxes)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen()
    print("Tic-Tac-Toe\n")
    show(boxes)
    print("\nIt's a draw!")

play()
