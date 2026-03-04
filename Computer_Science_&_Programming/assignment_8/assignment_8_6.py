import random

def making_choice():
    choice = input("Insert your entry (scissors, rock, paper): ")
    while choice != "scissors" and choice != "rock" and choice != "paper":
        choice = input("Invalid entry, please insert a valid entry: ")
    return choice

def pc_choosing():
    random_choice = random.randint(1, 3)
    if random_choice == 1:
        return "scissors"
    elif random_choice == 2:
        return "rock"
    elif random_choice == 3:
        return "paper"

def is_it_a_tie(a, b):
    return a == b

def player_win(a, b):
    if a == "scissors" and b == "paper":
        return True
    elif a == "paper" and b == "rock":
        return True
    elif a == "rock" and b == "scissors":
        return True
    else:
        return False

def more_wins(a, b):
    if a > b:
        return "USER"
    elif a < b:
        return "PC"
    else:
        return "TIE"

if __name__ == '__main__':

    #The user must first specify the number of games to be played.
    numbers_of_games = int(input("How many matches do you want to play? "))

    count_player_wins = 0
    count_pc_wins = 0

    for n_game in range(numbers_of_games):

        current_game_still_going = True
        print(f"\nGame {n_game}\n---")

        choice_pc = "no_choice"
        choice = "no_choice"

        while current_game_still_going:
            choice = making_choice()
            choice_pc = pc_choosing()

            if is_it_a_tie(choice, choice_pc):
                print(f"Tie! Both players played '{choice}'")
                continue
            else:
                current_game_still_going = False

        print(f"pc plays: {choice_pc}")

        if player_win(choice, choice_pc):
            print("USER WINS!")
            count_player_wins += 1
        else:
            print("PC WINS!")
            count_pc_wins += 1

    print(f"\n---")
    print(f"The overall winner is: {more_wins(count_player_wins, count_pc_wins)}!")
    print(f"User won {count_player_wins} time(s), on avarage {((count_player_wins/numbers_of_games)*100):.2f}%")
    print(f"PC won {count_pc_wins} time(s), on avarage {((count_pc_wins/numbers_of_games)*100):.2f}%")