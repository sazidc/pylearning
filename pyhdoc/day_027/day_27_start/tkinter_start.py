# # Tkinter - Graphical User Interface

from tkinter import Button, Label, Tk, Entry

def button_clicked():
    print("I got clicked")
    my_label.config(text = input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="I AM SPARTA")

# Button

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()




window.mainloop()