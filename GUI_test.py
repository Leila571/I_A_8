from tkinter import*
import what_key_questions
root = Tk()
root.geometry("500x500")
"""""
def dropdownmenu():
    #root.config(text="Select Game").grid()
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
"""""
def question():
    my_string_var.set("Choose a question")

btn_2 = Button(root,
               text = "Questions",
               command = question)

def submit_btn():


entry_box_1 = tk.Entry(root)
entry_box_1.grid(row=3, column=8)
submit_btn_1 = tk.Button(root, text='Submit', command=submit_btn)
submit_btn_1.grid(row=4, column=8)
# \n for line break
# create a StringVar class
my_string_var = StringVar()

# set the text
my_string_var.set("What is the order of sharps?")

# create a label widget
my_label = Label(root,
                 textvariable=my_string_var)

def dropdownmenu():

    what_key_questions.pack_questions_2d()
    what_key_questions.shuffle()


Button(root, text="Time Signatures!", command=dropdownmenu).grid(row=1, column=7)
# sticky.grid(sticky=W)
Button(root, text="What Key Is This?", command=dropdownmenu).grid(row=3, column=7)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Era!", command=dropdownmenu).grid(row=4, column=7)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Genre!", command=dropdownmenu).grid(row=5, column=7)
# sticky.grid(sticky=W)

btn_2.grid(row=1, column=8)
my_label.grid(row=2, column=8)
root.mainloop()
