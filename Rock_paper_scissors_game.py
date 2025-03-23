
import random

rps_dict = ('r', 'p', 's')
emojis = { 'r': '🪨', 's': '✂️', 'p': '📃'}

while True:

    player_choice = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()

    if player_choice not in rps_dict:
        print('Invalid choice')
        continue

    computer_choice = random.choice(rps_dict)

    print(f"You choose {emojis[player_choice]}")
    print(f"Computer choose {emojis[computer_choice]}\n")


    if player_choice == computer_choice:
        print("Draw")

    elif ((player_choice == "r" and computer_choice == "s") or
          (player_choice == "s" and computer_choice == "p") or
          (player_choice == "p" and computer_choice == "r")):
        print("\033[32mYou Win!\033[0m")

    else:
        print("\033[31mYou Lose!\033[0m")


    user_input = input("Do you wish to continue (y/n): ").strip().lower()
    if user_input == "n":
        print("Thank you and goodbye!")
        break








