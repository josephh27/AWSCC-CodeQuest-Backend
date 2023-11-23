from random import randrange
print("This a game of rock, paper, and scissors.")
while True:
    possible_attacks = ["r", "p", "s"]
    player1_input = input("What is your attack? (r)ock, (p)aper, or (s)cissors? ").lower()
    if player1_input not in possible_attacks:
        print("Please answer only the initial of your attack.")
    else:
        break
player2_input = possible_attacks[randrange(3)]
if player1_input == player2_input:
    print("It is a tie!")
elif player1_input == "r":
    if player2_input == "s":
        print("You win!")
    else:
        print("You lose!")
elif player1_input == "p":
    if player2_input == "r":
        print("You win!")
    else:
        print("You lose!")
elif player1_input == "s":
    if player2_input == "p":
        print("You win!")
    else:
        print("You lose!")
    
