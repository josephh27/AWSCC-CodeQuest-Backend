class MiniProgram:
    def __init__(self):
        pass
    def evaluateNumber(self, number):
        if (number == 0):
            return f"That number is a Zero"
        elif (number > 0):
            return f"{number} is a Positive number!"
        elif (number < 0):
            return f"{number} is a Negative number!"
        

mini_challenge1 = MiniProgram()
chall1_ans = int(input("Enter a number: "))
challenge1_answer = mini_challenge1.evaluateNumber(chall1_ans)
print(challenge1_answer)

class MainChallenge:
    def __init__(self):
        pass
    def enter_adventure(self):
        print("You are wandering through a forest and you see a cave...")
        print("Note: Any answer aside from N will be considered as Yes")
        answer = input("Do you enter the cave (Y/N)? ").upper()
        if answer == "Y":
            print("You saw a goblin with a lot of weapons...")
            answer = input("Do you attack it (Y/N)? ").upper()
            if answer == "Y":
                print("You died due to lack of weapons.")
            else: 
                print("You saw a lot of weapons laying down in front of you...")
                answer = input("Do you pick up the weapons (Y/N)? ").upper()
                if answer == "Y":
                    print("Congratulations! You survived the cave as you encountered the goblin again and slayed it using the weapons!")
                else:
                    print("You died afterwards as you encountered the goblin again without having any weapons.")
        else:
            print("You see a big foot wandering...")
            answer = input("Do you attack the big foot (Y/N)? ").upper()
            if answer == "Y":
                print("You died due to lack of weapons.")
            else:
                print("You saw a lot of weapons laying down in front of you...")
                answer = input("Do you pick up the weapons (Y/N)? ").upper()
                if answer == "Y":
                    print("Congratulations! You survived the cave as you encountered the big foot again and slayed it using the weapons!")
                else:
                    print("You died afterwards as you encountered the big foot again without having any weapons.")

main_challenge = MainChallenge()
main_challenge.enter_adventure()
    