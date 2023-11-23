print("This is a FizzBuzz generator.")
while True:
    try:
        limit = int(input("Please input a limit: "))
        for i in range(1, limit + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            if output == "":
                output = i
            print(output)
        break
            
    except:
        print("Please input a valid limit.")
        