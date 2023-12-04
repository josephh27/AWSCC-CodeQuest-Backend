# Replicating Attribute Error
try:
    number = 5
    number.append(3)
except AttributeError:
    print("Attribute Error Raised!")

# Replicating Key Error
try:
    my_dict = {
        "name": "Joseph",
        "age": 20
    }
    print(my_dict['address'])
except KeyError:
    print("Key Error Raised!")

# Replicating Name Error
try:
    print(awesome)
except NameError:
    print("Name Error Raised!")

# Replicating Syntax Error
try: 
    eval("x === x")
except SyntaxError:
    print("Syntax Error Raised!")
    


