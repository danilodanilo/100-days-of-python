import tkinter
from tkinter import END

window = tkinter.Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)
# adds space between widgets and the border of the window. This can be done in each widget individually
window.config(padx=20, pady=20)

# LABEL
my_label = tkinter.Label(text="My Label", font=("Arial", 24, "bold"))
# the pack method makes the label appear in the UI. It can combine a few parameters to be able to
# position correctly the text
# my_label.place(x=0, y=0)  # place it in the exact desire position
# pack() cannot be used along with grid
my_label.grid(column=0, row=0)
# my_label["text"] = "New Text"


# BUTTON
# def button_clicked():
#     my_label["text"] = "Text changed on click"
#
#
# button = tkinter.Button(text="Click Me!", command=button_clicked)
# button.pack()

# ENTRY OR INPUT
def input_value_clicked():
    typed_value = input_box.get()
    my_label["text"] = typed_value


input_box = tkinter.Entry(width=30)
input_box.insert(END, string="Some text")
button = tkinter.Button(text="Click Me!", command=input_value_clicked)
button2 = tkinter.Button(text="Click Me 2!")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)
input_box.grid(column=3, row=2)
#button.pack()
#input_box.pack()

# TEXT
text = tkinter.Text(height=5, width=30)
# puts the cursor on the textbox
text.focus()
text.insert(END, "Example of multi-line box")
# Gets the current value in the textbox, starting at line 1, character zero...that is why the 1.0
print(text.get("1.0", END))
#text.pack()


# SPINBOX

def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
#spinbox.pack()


# Scale
# Called with the current scale value
def scaled_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scaled_used)
#scale.pack()


# CHECKBUTTON
def checkbutton_used():
    # Prints 1 if On button is checked, otherwise 0
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checked_state.get()
#checkbutton.pack()


# RADIO BUTTON

def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
#radiobutton1.pack()
#radiobutton2.pack()


# LISTBOX
def list_box_used(event):
    print(list_box.get(list_box.curselection()))


list_box = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    list_box.insert(fruits.index(item), item)
list_box.bind("<<ListboxSelect>>", list_box_used)
#list_box.pack()
window.mainloop()
