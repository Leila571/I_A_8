from tkinter import*
import musical_era_questions
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

root.mainloop()
