from tkinter import*
import musical_era_questions
#import  what_key_questions
root = Tk()
root.title('The Music Theory Game')
root.geometry("800x500")




#if text_entry_var == string_to_compare :
   # print("correct")
#else:
   # print("incorrect")
def question():
    my_string_var.set("Choose a question")


btn_2 = Button(root,
               text = "Questions",
               command = question)


temp = StringVar()
entry_box_1 = Entry(root,textvariable=temp)
entry_box_1.grid(row=3, column=15)

counter = 0
#takes questions from musical_era_questions.py and shuffles them
#make sure it only shuffles once on first button press
questions_from_2d_array = musical_era_questions.shuffle()



def submit_btn():
    global counter

    #assesses question length and makes sure questions and answers don't get mixed in with other questionsns
    question_length = len(questions_from_2d_array)
    #assesses question length and prints questions as a pack in terminal
    print(question_length)
    print (questions_from_2d_array)
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
        local_string = temp.get()
        #prints the text from text entry box in terminal
        print (local_string,"line 85")
        #creates message that tells user what they typed in to the text entry box
        my_string_var.set("you put in  "+local_string)
        my_string_var_2.set(question)
        #assesses if answer is correct or not. if statement prints "good" in terminal if anc is correct
        #questions out of sync
        print (anc,"line 90")
        print(local_string, "line 91")
        if anc_2 == local_string:
            print("good")
        #prints "bad" in terminal if user input is incorrect
        else:
            print("bad")
        counter = counter + 1
    temp.set("")




def entry_box_1():
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
btn_2.grid(row=1, column=15)
my_label.grid(row=2, column=15)
my_label_2.grid(row=2, column=16)

root.mainloop()
