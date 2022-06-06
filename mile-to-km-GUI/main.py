from tkinter import *


def convert_miles_to_km():
    miles = float(input_miles.get())
    number = 1.609
    km = miles * number
    my_label2["text"] = km


window = Tk()
window.config(padx=20, pady=20)
window.title("Miles to Km program")
window.geometry("240x100")
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)
input_miles_label = Label(text="Miles")
input_miles_label.grid(column=2, row=0)
my_label = Label(text="Is equal to")
my_label.grid(column=0, row=1)
my_label2 = Label()
my_label2.grid(column=1, row=1)
my_label3 = Label(text="km")
my_label3.grid(column=2, row=1)
#my_label2.pack()
button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)
#button.pack()
window.mainloop()
