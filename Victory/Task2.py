# A PROGRAM FOR USER DATA VALIDATION
##
#

# import random and string for creating random strings

import random
import string

random.choice(string.ascii_lowercase)
s = ''.join([random.choice(string.ascii_lowercase) for i in range(5)])
# create an empty list to serve as your container

user_details = []

# Start your while statement for looping through and adding user details
user_number = 1  # for indicating serial number of users
new_user = True
length_password = True
while True:
    first_name = input('what is your first name: ')
    last_name = input('what is your last name: ')
    Email = input('Please enter your email address: ')
    password = first_name[0:2] + last_name[-2:] + s
    print("Your password is", password)
    choice = input("Are you alright with the password? Enter Yes or No ")
    if choice == "Yes":
        print("Thank you for logging in")
    elif choice == "no":
        new_password = input("Enter another password more than or equal to 7 values: ")
        new_password = password

        if len(new_password) <= 7:
            print("password must be more than or equal to 7")
            new_password = input("Enter another password more than or equal to 7 values: ")
        else:
            print("Thank you for logging in")

    user = {'first_name': first_name,
            'last_name': last_name,
            'Email': Email,
            'password': password}
    user_data = "user" + str(user_number), "details:", user
    user_details.append(user_data)
    user_number = user_number + 1
    cont = input("Do you want to add another user? Enter yes or no ")
    if cont == "no":
        break
print(user_details)
