# userinput = input("Please enter a number: ")
# if userinput == "1":
# elif userinput == "2":
# print("Thank you for trusting us")
#  print("I love you")
# else:
 # print("You did not enter a valid number!")
# try:
# userInput1 = int(input("Please enter a number: "))
# userInput2 = int(input("Please enter another number: "))
# answer = userInput1 / userInput2
# print("The answer is ", answer)
# except ValueError:
# print("Error: You did not enter a number")
# except ZeroDivisionError:
# print("Error: Cannot divide by zero")
# except Exception as e:
# print("Unknown error: ", e)


def checkifprime(number):
    for x in range(2, number):
        if (number%x == 0):
            return False
    return True


answer = checkifprime(0)
print(answer)


