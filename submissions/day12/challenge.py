class Dog:
    def __init__(self, name, breed, color, age):
        self.__name = name
        self.__breed = breed
        self.__color = color
        self.__age = age

    def bark(self):
        print("Woof Woof!")

    def show_details(self):
        print(f"Name: {self.__name}\nBreed: {self.__breed}\nColor: {self.__color}\nAge: {self.__age}")

if __name__ == "__main__":
    my_dog = Dog("Michico", "Dachshund", "Brown", 4)
    my_dog.bark()
    my_dog.show_details()