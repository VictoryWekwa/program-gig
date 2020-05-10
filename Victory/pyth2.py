#
# A PROGRAM FOR USER DATA VALIDATION
#
import random
import string
random.choice(string.ascii_lowercase)
s = ''.join([random.choice(string.ascii_lowercase) for i in range(5)])  # for getting random string
# Create an empty dictionary
user_details = {}
new_user = True
while True:
    user_details["first_name"] = [input('what is your first name: ')]
    user_details["last_name"] = [input('what is your last name: ')]
    user_details["Email"] = [input('Please enter your email address: ')]

    password = "first_name"[0:2] + "last_name"[-2:] + s
    print("Your password is", password)
    display_message = input("Are you alright with the password? Enter Yes or no to get another password ")

    if display_message == "Yes":
        print("Thank you for logging in")
    elif display_message == "no":
        new_password = input("please enter another password more than or equal to 7: ")
        new_password = password
        if len(new_password) < 7:
            print("Password invalid! Please enter another password")
            new_password = input("please enter another password more than or equal to 7: ")
    print(user_details)
    cont = input("Do you want to add another user?Enter Yes or No ")
    if cont == "no":
        break
print(user_details)
