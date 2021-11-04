import time_sig_questions
def play_game():
    print("play game")
    questions_array=time_sig_questions.shuffle()
    print(questions_array)
    number_of_tries=len(questions_array)
    print(number_of_tries)
    for tries in range(number_of_tries):
       # print(questions_array[tries][0])
        answer=questions_array[tries][2]
        user_answer=input(questions_array[tries][0])
        if user_answer==answer:
            print("success!")
        else:
            print("wrong!")
            print("the right answer is",answer)

play_game()
