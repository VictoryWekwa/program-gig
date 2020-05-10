try:
    import MyPythonFuctions as m
    username = input(" Please enter your username to start : ")
    userScore = int(m.get_user_point(username))
    if userScore == -1:
        new_user = True
        userScore = 0
    else:
        new_user = False
    user_choice = 0
    while user_choice != "-1":
        userScore += m.generate_question()
        print("Your score is", userScore)
        user_choice = input(" Please click on Enter to continue the questions or -1 to exit")
    m.update_user_point(new_user, username, str(userScore))
except Exception as error:
    print("The question will exit now because an error. Thank you")


