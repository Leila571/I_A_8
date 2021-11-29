
import questions
from tkinter import *
#import  what_key_questions
root = Tk()
root.title('The Music Theory Game')
root.geometry("800x500")

temp = StringVar()
entry_box_1 = Entry(root,textvariable=temp)
entry_box_1.grid(row=3, column=15)
counter = 0
score =0

def get_questions():
    global questions_from_2d_array
    questions_from_2d_array = musical_era_questions.shuffle()
get_questions()
def question_fun(counter):
    question = questions_from_2d_array[counter][1]
    print(questions_from_2d_array[counter][3])
    my_string_var.set(question)

#del later
print(questions_from_2d_array)

def submit_btn():
    global counter
    global score
    question_length = len(questions_from_2d_array)

    if counter <  question_length:

        #print(questions_from_2d_array[counter][1],"77")
        question = questions_from_2d_array[counter][1]


        #print(questions_from_2d_array[counter][3],"79")
        #use this to remove \n
        anc = questions_from_2d_array[counter][3].rstrip()

        local_string = temp.get()
        print(local_string.rstrip())

        my_string_var_2.set("your put "+ local_string)

        if anc == local_string:
            my_string_var_2.set("your put " + local_string + " correct")
            score = score + 1
            print(score," score")

        else:
            my_string_var_2.set("wrong " + anc )


        counter = counter + 1
        if counter < question_length:
            question_fun(counter)

    # clears the box
    temp.set("")


my_string_var = StringVar()
my_string_var_2 = StringVar()
my_string_var.set("")

# create a label widget
my_label = Label(root,textvariable=my_string_var)
my_label_2 = Label(root,textvariable=my_string_var_2)

submit_btn_1 = Button(root, text='Submit', command=submit_btn)
submit_btn_1.grid(row=4, column=15)

'''
Button(root, text="Time Signatures!", command=dropdownmenu).grid(row=1, column=7)
# sticky.grid(sticky=W)
Button(root, text="What Key Is This?", command=dropdownmenu).grid(row=1, column=8)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Era!", command=dropdownmenu).grid(row=1, column=9)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Genre!", command=dropdownmenu).grid(row=1, column=10)
# sticky.grid(sticky=W)
'''
Questions_btn = Button(root,text = "Questions",command = question_fun)
Questions_btn.grid(row=1, column=15)

my_label.grid(row=2, column=15)
my_label_2.grid(row=2, column=16)

question_fun(counter)

def musical_era_questions():
    print("musical_era.txt")

def time_sig_questions():
    print("time_sigs.txt")

def what_key_questions():
    print("What_key.txt")

def musical_genre_questions():
    print("musical_genre.txt")


#if text_entry_var == string_to_compare :
   # print("correct")
#else:
   # print("incorrect")
def choose_a_question():
    my_string_var.set("Choose a question")


btn_2 = Button(root,
               text = "Questions",
               command = choose_a_question)


anc_string_variable = StringVar()
anc_entry_box_1 = Entry(root,textvariable=anc_string_variable)
anc_entry_box_1.grid(row=3, column=15)

counter = 0
#takes questions from questions.py and shuffles them
#make sure it only shuffles once on first button press
#questions_from_2d_array = musical_era_questions.shuffle()
questions_from_2d_array = questions.shuffle1()


def submit_btn():
    global counter

    #assesses question length and makes sure questions and answers don't get mixed in with other questionsns
    question_length = len(questions_from_2d_array)
    #assesses question length and prints questions as a pack in terminal
    print(question_length)
    print(questions_from_2d_array)
    #this forloop prints the questions and answers
    #submit button should trigger a counter for scorekeeping and call next question
    if counter <  question_length:

        print(counter)

        # string compare here
        #prints questions in terminal
        print(questions_from_2d_array[counter][1],"77")
        question = questions_from_2d_array[counter][1]
        anc_2 = questions_from_2d_array[counter][3]
        # set the text
        my_string_var.set("test")
        #prints answers in terminal
        print(questions_from_2d_array[counter][3],"79")
        #prints answer as string
        anc = questions_from_2d_array[counter][3]
        #gets the text from text entry box and prints in terminal
        local_string = anc_string_variable.get()
        #prints the text from text entry box in terminal
        print(local_string,"line 85")
        #creates message that tells user what they typed in to the text entry box
        my_string_var.set("you put in  "+local_string)
        my_string_var_2.set(question)
        #assesses if answer is correct or not. if statement prints "good" in terminal if anc is correct
        #questions out of sync
        print(anc,"line 90")
        print(local_string, "line 91")
        if anc_2 == local_string:
            print("good")
        #prints "bad" in terminal if user input is incorrect
        else:
            print("bad")
        counter = counter + 1
    anc_string_variable.set("")




def anc_entry_box_1():
    #local_string = entry_box_1.get()
    #print (local_string)
    #my_string_var.set(local_string)
    print("getting user input")

# \n for line break
# create a StringVar class
my_string_var = StringVar()
my_string_var_2 = StringVar()
# set the text
my_string_var.set("")

# create a label widget
my_label = Label(root,
                 textvariable=my_string_var)
my_label_2 = Label(root,
                 textvariable=my_string_var_2)


#def dropdownmenu():

#    what_key_questions.pack_questions_2d()
#    what_key_questions.shuffle()

submit_btn_1 = Button(root, text='Submit', command=submit_btn)
submit_btn_1.grid(row=4, column=15)


Button(root, text="Time Signatures!", command=time_sig_questions).grid(row=1, column=7)
# sticky.grid(sticky=W)
Button(root, text="What Key Is This?", command=what_key_questions).grid(row=1, column=8)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Era!", command=musical_era_questions).grid(row=1, column=9)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Genre!", command=musical_genre_questions).grid(row=1, column=10)
# sticky.grid(sticky=W)

btn_2.grid(row=1, column=15)
my_label.grid(row=2, column=15)
my_label_2.grid(row=2, column=16)

root.mainloop()
