class Program:
    def __init__(self):
        pass
    def computeSum(self, numbers):
        result = 0
        for number in numbers:
            result += number
        return result

my_program = Program()
while True:
    number_arguments = []
    numbers_count = int(input("How many numbers do you wish to input? "))
    for i in range(numbers_count):
        number = int(input("Please input a number: "))
        number_arguments.append(number)
    print(my_program.computeSum(number_arguments))
    while True: 
        isContinue = input("Do you wish to try again? Y/N")
        if isContinue.lower() == "n":
            exit()
        elif isContinue.lower() == "y":
            break
        else:
            pass
        

    
    

