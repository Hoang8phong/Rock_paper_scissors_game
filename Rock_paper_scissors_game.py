import random
count_lose = 0
count_win = 0
count_draw = 0
player1_score = 0
player2_score = 0
player_draw = 0
rps = ['r', 'p', 's']
rps_dict = {
    "r": "🪨",
    "p": "📃",
    "s": "✂️"
}

#Condition check winner
def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif  (player_choice == 'r' and computer_choice == 'p') or \
          (player_choice == 'p' and computer_choice == 's') or \
          (player_choice == 's' and computer_choice == 'r'):
        return "lose"
    else:
        return "win"

#Function vs computer
def vs_computer():
    global count_lose, count_win, count_draw
    while True:
        #Player choice
        player_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()

        #Check if choice is invalid
        if player_choice not in rps:
            print('Invalid choice! pls enter again')
            continue

        #Computer random choice
        computer_choice = random.choice(rps)

        #Print player and computer choice
        icon_player_convert = rps_dict[player_choice]
        icon_computer_convert = rps_dict[computer_choice]
        print(f'You chose {icon_player_convert}')
        print(f'Computer chose {icon_computer_convert}')

        result = check_winner(player_choice,computer_choice)

        if result == 'draw':
            print("Draw")
            count_draw += 1
        elif result == 'lose':
            print("\033[31m YouLose\033[0m")
            count_lose += 1
        else:
            print("\033[32mYou Win\033[0m")
            count_win += 1

        print(f'''Current score:
------------------
\033[32mWins\033[0m:  {count_win}
\033[31mLoses\033[0m: {count_lose}
Draws: {count_draw}
------------------''')

        #Ask if player want to continue
        continue1 = input('Continue (y/n): ').lower()
        if continue1 == 'n':
           print('Goodbye and see you again<3')
           print(f'Final score: \033[32mWins\033[0m: {count_win}, \033[31mLoses\033[0m: {count_lose}, Draws: {count_draw}')
           break
        elif continue1 != 'y':
           print('Invalid choice, please enter again!')

#Function vs Human
def vs_human():
    global player1_score, player2_score, player_draw

    while True:
        player1_choice = input('Player 1 chose rock, paper, or scissors? (r/p/s): ')
        player2_choice = input('Player 2 chose rock, paper, or scissors? (r/p/s): ')

        if player1_choice not in rps or player2_choice not in rps:
            print('Invalid choice! pls enter again')
            continue
        player1_icon = rps_dict[player1_choice]
        player2_icon = rps_dict[player2_choice]
        print(f'Player 1 chose {player1_icon}')
        print(f'Player 2 chose {player2_icon}')

        if player1_choice == player2_choice:
            print("Draw")
            print("----------")
            player_draw += 1
        elif check_winner(player1_choice, player2_choice) == 'win':
            print("Player 1 win")
            print("----------")
            player1_score += 1
        else:
            print("Player 2 win")
            print("----------")
            player2_score += 1

        print(f'''Current score
------------------------
Player 1: {player1_score}
Player 2: {player2_score}
Draws:    {player_draw}
------------------------''')

        player1_continue = input("Player 1 continue? (y/n): ").lower()
        player2_continue = input("Player 2 continue? (y/n): ").lower()

        if player1_continue == 'n' and player2_continue == 'n':
            print('Thank you and goodbye<3')
            print(f'Final score: Player 1: {player1_score}, Player 2: {player2_score}, Draws: {player_draw}')
            if player1_score > player2_score:
                print('\033[32mPlayer 1 Win\033[0m')
            elif player1_score == player2_score:
                print('Draw')
            else:
                print('\033[32mPlayer 2 Win\033[0m')
            break
        elif player1_continue != player2_continue:
            print('Both player need to choose the same option (y/n)!!! ')


print(''' Welcome to Rock Paper Scissor game
--------> Choose 1 to play vs computer
--------> Choose 2 to play vs your human friend:)
--------> Choose 3 to Exit''')

while True:
    game_mode = input("Choose here >> ")

    if game_mode == '1':
        print("Vs Computer")
        vs_computer()
        break
    elif game_mode == '2':
        print("2 players game")
        vs_human()
        break
    elif game_mode == '3':
        print('Bye')
        break
    else:
        print("Invalid Input, please try again!")








