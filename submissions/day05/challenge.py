import random
possible_attacks = ["rock", "paper", "scissor"]
print("This is a rock, paper, and scissors game.")
while True:
    user_input = input("What is your attack (rock, paper, scissor): ").lower()
    if user_input not in possible_attacks:
        print("Please input a valid attack.")
    else:
        break
opponent_attack = random.choice(possible_attacks)
if user_input == opponent_attack:
    print("It is a tie!") 
elif user_input == "rock":
    if opponent_attack == "scissor":
        print("You win!")
    else:
        print("You lose!")
elif user_input == "paper":
    if opponent_attack == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user_input == "scissor":
    if opponent_attack == "paper":
        print("You win!")
    else:
        print("You lose!")
