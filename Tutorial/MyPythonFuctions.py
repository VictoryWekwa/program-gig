from random import randint
from os import remove, rename


def get_user_point(username):
    try:
        f = open('userScores.txt', 'r')
        for line in f:
            content = line.split(",")
            if content[0] == username:
                f.close()
            return content[1]
        f.close()
        return "-1"
    except IOError:
        print("\nFile userScores.txt not found. A new file will be created.")
        f = open('userScores.txt', 'w')
        f.close()
        return "-1"


def update_user_point(new_user, username, score):
    if new_user:
        f = open('userScores.txt', 'a')
        f.write('\n' + username + ', ' + score)
        f.close()
    else:
        f = open('userScores.txt', 'r')
        output = open('userScores.tmp', 'w')
    for line in f:
        content = line.split(',')
        if content[0] == username:
            content[1] = score
            line = content[0] + ', ' + content[1] + '\n'
            output.write(line)
    f.close()
    output.close()
    remove('userScores.txt')
    rename('userScores.tmp', 'userScores.txt')


def generate_question():
    operand_list = ['0', '0', '0', '0', '0']
    operator_list = ['', '', '', '']
    operator_dict = {1: "+", 2: "-", 3: "*", 4: "**"}
    for index in range(0, 5):
        operand_list[index] = randint(1, 9)
    for index in range(0, 4):
        if index > 0 and operator_list[index-1] != "**":
            operator = operator_dict[randint(1, 4)]
        else:
            operator = operator_dict[randint(1, 3)]
        operator_list[index] = operator
    question_string = str(operand_list[0])
    for index in range(1, 5):
        question_string = question_string + str(operand_list[index]) + operator_list[index-1]
        result = eval(question_string)
        question_string = question_string.replace("**", "^")
        print('\n' + question_string)
    user_answer = input("Please enter your answer: ")
    while True:
        try:
            if int(user_answer) == result:
                print("Excellent")
                return 1
            else:
                print(r"Wrong answer, the correct answer is", result)
                return 0
        except Exception as error:
            print("Error in your answer")
            user_answer = input("Please enter a number : ")




