from audioplayer import AudioPlayer
import time
from tkinter import *

import time_sig_questions
import what_key_questions
import musical_era_questions
import musical_genre
import What_key

root = Tk()
root.geometry("500x500")
count = 0


def play():
    print("Playing audio.")
    # Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
    AudioPlayer("Test.mp3").play(block=False)


def stop():
    print("Stopping audio.")
    # Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
    # AudioPlayer("Test.mp3").play(block=True)
    AudioPlayer("Test.mp3").stop()


def sticky():
    print("sticky")


def dropdownmenu():
    root.config(text="Select Game").grid()
    options = [
        "Time Signatures!",
        "What Key Is This?",
        "Guess the Music Era!",
        "Guess the Music Genre",
    ]
    clicked = StringVar()
    clicked.set("Time Signatures!")
    clicked.set("What Key Is This?")
    clicked.set("Guess the Music Era!")
    clicked.set("Guess the Music Genre!")
    drop = OptionMenu(root, clicked, *options)
    drop.grid()


def welcome():
    print("Welcome to The Music Theory Game!")
    win = Canvas(root, row="3", column="9")
    win.grid()


def time_signatures():
    print("Welcome to time signatures!")
    # pop up window
    # questions with audio snippets
    # scorekeeping


# def questions():
#    global count
#    anc = time_sig_questions.Time_signatures_question_1()
#    count = count + anc[0]
#    print(anc[0],anc[1], anc[2])
#    print(count)
#    anc = time_sig_questions.Time_signatures_question_2()
#    count = count + anc[0]
#    print (anc[0],anc [1], anc[2])
#    print(count)
#    anc = time_sig.Time_signatures_question_3()
#    count = count + anc[0]
#    print (anc[0],anc [1], anc[2])
#    print(count)
#    anc = time_sig.Time_signatures_question_4()
#    count = count + anc[0]
#    print (anc[0],anc [1], anc[2])
#    print(count)
#    anc = time_sig.Time_signatures_question_5()
#    count = count + anc[0]
#    print (anc[0],anc [1], anc[2])
#    print(count)
#
# questions()

def questions1():
    global count
    anc = What_key.What_key_question_1()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = What_key.What_key_question_2()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = What_key.What_key_question_3()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = What_key.What_key_question_4()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = What_key.What_key_question_5()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)


#questions1()


def questions2():
    global count
    anc = Musical_era.Musical_era_question_1()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = Musical_era.Musical_era_question_2()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = Musical_era.Musical_era_question_3()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = Musical_era.Musical_era_question_4()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)
    anc = Musical_era.Musical_era_question_5()
    count = count + anc[0]
    print(anc[0], anc[1], anc[2])
    print(count)


def play_game_time_sig():
    print("line 142 in Sound play game")
    time_sig_questions.pack_questions_2d()
    questions_array = time_sig_questions.shuffle()
    print(questions_array)
    number_of_tries = len(questions_array)
    print(number_of_tries)
    for tries in range(number_of_tries):
        #print(questions_array[tries][0])
        answer = questions_array[tries][2]
        print("playing music listen for time signature")
        print((questions_array[tries][0]))
        AudioPlayer((questions_array[tries][1]).rstrip()).play(block=True)
        user_answer = input(questions_array[tries][0])
        if user_answer == answer:
            print("success!")
        else:
            print("wrong!")
            print("the right answer is", answer)


play_game_time_sig()

def play_game_what_key():
    print("line 165 in Sound play game")
    what_key_questions.pack_questions_2d()
    questions_array = what_key_questions.shuffle()
    print(questions_array)
    number_of_tries = len(questions_array)
    print(number_of_tries)
    for tries in range(number_of_tries):
        #print(questions_array[tries][0])
        answer = questions_array[tries][2]
        print("playing music listen for key").set()
        print((questions_array[tries][0]))
        AudioPlayer((questions_array[tries][1]).rstrip()).play(block=True)
        user_answer = input(questions_array[tries][0])
        if user_answer == answer:
            print("success!")
        else:
            print("wrong!")
            print("the right answer is", answer)


play_game_what_key()

def play_game_musical_era():
    print("line 188 in Sound play game")
    musical_era_questions.pack_questions_2d()
    questions_array = musical_era_questions.shuffle()
    print(questions_array)
    number_of_tries = len(questions_array)
    print(number_of_tries)
    for tries in range(number_of_tries):
        #print(questions_array[tries][0])
        answer = questions_array[tries][2]
        print("playing music listen for era")
        print((questions_array[tries][0]))
        AudioPlayer((questions_array[tries][1]).rstrip()).play(block=True)
        user_answer = input(questions_array[tries][0])
        if user_answer == answer:
            print("success!")
        else:
            print("wrong!")
            print("the right answer is", answer)


play_game_musical_era()

def play_game_musical_genre():
    print("line 211 in Sound play game")
    musical_genre.pack_questions_2d()
    questions_array = musical_genre.shuffle()
    print(questions_array)
    number_of_tries = len(questions_array)
    print(number_of_tries)
    for tries in range(number_of_tries):
        #print(questions_array[tries][0])
        answer = questions_array[tries][2]
        print("playing music listen for genre")
        print((questions_array[tries][0]))
        AudioPlayer((questions_array[tries][1]).rstrip()).play(block=True)
        user_answer = input(questions_array[tries][0])
        if user_answer == answer:
            print("success!")
        else:
            print("wrong!")
            print("the right answer is", answer)


play_game_musical_genre()

"""
def What_Key_question_1():
    global score
    print("Can you identify the key of this song?")
    a = input("Question 1: What is the key of this song")
    # import audio file of We're Going Wrong here
    if "minor" in a:
        score = score + 1
        print("Correct!")
    else:
        print("Wrong! It's minor!")
        print("You have finished and scored", score, "out of 5")
"""


# create root window
# Button(root, text = "startButton", command = play).grid(row=0, column=5)
# Button(root, text = "stopButton", command = stop).grid(row=1, column=5)



# GUI
Button(root, text="Time Signatures!", command=dropdownmenu).grid(row=1, column=7)
# sticky.grid(sticky=W)
Button(root, text="What Key Is This?", command=dropdownmenu).grid(row=3, column=7)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Era!", command=dropdownmenu).grid(row=4, column=7)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Genre!", command=dropdownmenu).grid(row=5, column=7)
# sticky.grid(sticky=W)
Button(root, text="Exit", command=dropdownmenu).grid(row=0, column=30)
# sticky.grid(sticky=W)

root.mainloop()
