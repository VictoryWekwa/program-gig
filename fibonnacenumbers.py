# A program to display the Fibonacci sequence to the nth term
##
#


def fibonacci(number_of_term):
    number_of_term = int(input("How many terms? : "))
# first two terms to start with
    term1, term2 = 1, 1
    count = 1
# Check if the number of terms is valid
    if number_of_term <= 1:
        print("Please enter a number greater than 1: ")
    elif number_of_term == 2:
        print("Fibonacci sequence up to", number_of_term, "is: ")
        print(term1)
    else:
        print("Fibonacci sequence is : ")
        while count < number_of_term:
            print(term1)
            nth_term = term1 + term2
    # update the values
            term1 = term2
            term2 = nth_term
            count += 1










