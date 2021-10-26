import random
from audioplayer import AudioPlayer

# lines = []

with open('time_sigs.txt') as f:
    lines = f.readlines()

# this builds a 2-d array called questions
number_of_questions = len(lines)
lines_per_question = 5
questions = [[" " for x in range(lines_per_question)] for y in range(lines_per_question)]


def pack_questions_2d():
    print("line 16 time_sig_questions_def pack question")
    #    lines_per_question = 5
    #    number_of_questions = len(lines)
    # this reads through the list one at a time
    count = 0
    for var in range(0, number_of_questions, lines_per_question):
        if 3 + var < number_of_questions:

            questions[count][0] = lines[0 + var]
            questions[count][1] = lines[1 + var]
            questions[count][2] = lines[2 + var]
            questions[count][3] = lines[3 + var]
            count = count + 1
        #AudioPlayer("Test.mp3").play(block=True)


#pack_questions_2d()


def shuffle():
    print("line 36 in time_sig_questions")
    random.shuffle(questions)
    return questions


#shuffle()
