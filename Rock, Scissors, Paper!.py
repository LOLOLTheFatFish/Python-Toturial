import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer choice {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "sissors":
            return "Rock smashes scissors! You win!"
        else:
            return "papers covers rock. You lose."
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! You win!"
        else:
            return "scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "rock":
            return "scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
        

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)