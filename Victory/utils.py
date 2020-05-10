def find_max(numbers):
    maximum = numbers[1]
    for number in numbers:
        if number > maximum:
         maximum = number
    return maximum