if __name__ == '__main__':
    with open("students.txt", 'r') as my_file:
        lines = sorted(my_file.readlines())
    with open("students.txt", 'w') as my_file:
       my_file.writelines(lines)
        

    