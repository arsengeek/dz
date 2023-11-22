size = 3
b1 = 0
b2 = 1
b3 = 2
p1 = 0
p2 = 1
p3 = 2
a1 = "-"
a2 = "-"
a3 = "-"
a4 = "-"
a5 = "-"
a6 = "-"
a7 = "-"
a8 = "-"
a9 = "-"

board = [a1, a2, a3, a4, a5, a6, a7, a8, a9]

def pole():
    print('    0   1   2')
    for i in range(size):
        print(f'{i} | {board[i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')

def game_step(index, player1):
    if (index > 9 or index < 1 or board[index - 1] in ('x', 'o')):
        return False
    return True

def win():
    combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for j in combinations:
        if all(board[i] == "x" for i in j):
            print("Победил X")
            pole()
            return True
        elif all(board[i] == 'o' for i in j):
            print("Победил O")
            pole()
            return True
    return False

def start_game():
    player1 = "x"
    step = 1


    while step < 10 and not win():
        pole()
        try:
            index = int(input("Ход первого игрока, введите номер поля: "))
            if index > 9:
                print("не допустимый вариант")
                continue

            if game_step(index, player1):
                print("Ход сделан")
                board[index - 1] = player1
                step += 1
                if (player1 == "x"):
                    player1 = "o"
                else:
                    player1 = "x"


            else:
                print("Невозможный ход")
        except:
            print("введите число")

print("Крестики-нолики")
start_game()

