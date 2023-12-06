# An example of abstraction
class Program:
    def __init__(self):
        pass
    def print_out(self, string):
        for char in string:
            print(char, end="")

    def print_out2(self, string):
        print(string)

# An example of inheritance
class SubProgram(Program):
    def get_str_length(self, string):
        return len(string)

if __name__ == '__main__':
    my_program = Program()
    my_program.print_out("Hello World\n")

    my_subprogram = SubProgram()
    my_subprogram.print_out2("Hello World")
    print(my_subprogram.get_str_length("okay"))