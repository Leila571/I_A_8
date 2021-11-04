from tkinter import *
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
# \n for line break
def dropdownmenu():
    print("dropdownmenu")
Button(root, text="Time Signatures!", command=dropdownmenu).grid(row=1, column=7)
# sticky.grid(sticky=W)
Button(root, text="What Key Is This?", command=dropdownmenu).grid(row=3, column=7)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Era!", command=dropdownmenu).grid(row=4, column=7)
# sticky.grid(sticky=W)
Button(root, text="Guess the Music Genre!", command=dropdownmenu).grid(row=5, column=7)
# sticky.grid(sticky=W)


root.mainloop()
