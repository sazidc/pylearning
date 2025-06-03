# # Miles to Kilometers in GUI

from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=50, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

kilometers = Label(text="0")
kilometers.grid(column=1, row=1)

kms_label = Label(text="Km")
kms_label.grid(column=2, row=1)


def miles_to_kms():
    miles = float(miles_input.get())
    kilometers.config(text=f"{round(miles * 1.609)}")


calculate_button = Button(text="Calculate", command=miles_to_kms)
calculate_button.grid(column=1, row=2)



window.mainloop()
