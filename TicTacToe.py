# Project: Tic Tac Toe Game

from prettytable import PrettyTable

a = PrettyTable()
a.align = 'c'
a.add_column("TIC", ["", "", ""])
a.add_column("TAC", ["", "", ""])
a.add_column("TOE", ["", "", ""])
a.header = True
a.border = True


p1 = "x"
p2 = "o"

print("WELCOME TO THE CLASSIC TIC TAC TOE GAME!\n")
print(f"Player1 plays with '{p1}' symbol. Player 2 plays as '{p2}'.")
print(f"Players are supposed to input the position they would like to place their symbol at.\nFor instance, if Player 1 inputs 12, the symbol will be placed as:\n")
a.rows[0][1] = 'x'
print(a, "\n")
print("Let's get started! All The Best! 😌\n")
a.rows[0][1] = ''
print(a)

c = 0


def game():
    global c
    if c % 2 == 0:
        print("Player 1:\n")
        user1 = input(f"Where would you like to place your '{p1}'? ")
        position = [int(user1[0]) - 1, int(user1[1]) - 1]
        if a.rows[position[0]][position[1]] == '':
            a.rows[position[0]][position[1]] = 'x'
            print(a)
            game_play = check()
            if game_play:
                c += 1
                game()
            else:
                print("Player 1 wins.")
                exit()
        else:
            print('This position is already occupied.')
            game()
    else:
        if c != 9:
            print("Player 2:\n")
            user2 = input(f"Where would you like to place your '{p2}'? ")
            position = [int(user2[0]) - 1, int(user2[1]) - 1]
            if a.rows[position[0]][position[1]] == '':
                a.rows[position[0]][position[1]] = 'o'
                print(a)
                game_play = check()
                if game_play:
                    c += 1
                    game()
                else:
                    print("Player 2 wins.")
                    exit()
            else:
                print('This position is already occupied.')
                game()
        else:
            print("CAT'S GAME : IT'S A TIE")


def check():
    if (a.rows[0][0] == a.rows[0][1] == a.rows[0][2] != '') or (a.rows[1][0] == a.rows[1][1] == a.rows[1][2] != '') or (a.rows[2][0] == a.rows[2][1] == a.rows[2][2] != '') or (a.rows[0][1] == a.rows[1][1] == a.rows[2][1] != '') or (a.rows[0][0] == a.rows[1][0] == a.rows[2][0] != '') or (a.rows[0][2] == a.rows[1][2] == a.rows[2][2] != '') or (a.rows[0][0] == a.rows[1][1] == a.rows[2][2] != '') or (a.rows[0][2] == a.rows[1][1] == a.rows[2][0] != ''):
        return False
    else:
        return True


game()
