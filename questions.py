import random

lines = []

with open('time_sigs.txt') as f:
    lines = f.readlines()

# this builds a 2-d array called questions
number_of_qustions = len(lines)
lines_per_question = 4
questions = [[" " for x in range(lines_per_question)] for y in range(lines_per_question)]

def pack_qustions_2d():
    print("pack")
    lines_per_question = 4
    number_of_qustions = len(lines)
    # this reads throught the list one at a time
    count = 0
    for var in range (0,number_of_qustions,lines_per_question):
        if 3+var < number_of_qustions:

            questions[count][0] = lines[0+var]
            questions[count][1] = lines[1+var]
            questions[count][2] = lines[2+var]
            questions[count][3] = lines[3+var]
            count = count + 1


def shuffle():
    print("shuffle")
    random.shuffle(questions)
    return questions

pack_qustions_2d()
shuffle()

