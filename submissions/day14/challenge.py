# Example of Polymorphism
class Calculator:
    def __init__(self):
        pass

    def add(self, nums):
        if len(nums) > 3:
            print("Cannot add more than 3 numbers")
            return
        sum = 0
        for num in nums:
            sum += num
        return sum
    
class ScientificCalculator(Calculator):
    def __init__(self):
        pass

    def add(self, nums):
        if len(nums) > 12:
            print("Cannot add more than 12 numbers")
            return
        sum = 0
        for num in nums:
            sum += num
        return sum

basic_calc = Calculator()
print(basic_calc.add([3,5,7]))

sci_calc = ScientificCalculator()
print(sci_calc.add([3,5,7,6,8]))


# Example of Encapsulation
class Dog:
    def __init__(self):
        self.__name = 'Bernard'

    def show_name(self):
        print(self.__name)

my_dog = Dog()
# Will raise an error
# print(my_dog.__name)

my_dog.show_name()
 

