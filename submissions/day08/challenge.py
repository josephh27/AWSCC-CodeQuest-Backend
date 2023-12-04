def get_average(numlist):
    sum = 0

    for number in numlist:
        sum += number

    avg = sum / len(numlist)

    return avg


list_1 = [3,5,72,23]
list_2 = [5, 56, 32, 43, 23]

print(get_average(list_1))
print(get_average(list_2))