from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    count = 0
    global reps
    reps = 0
    minutes, secs = divmod(count, 60)
    time_format = '{:02d}:{:02d}'.format(minutes, secs)
    canvas.itemconfig(timer_text, text=time_format)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", fg=RED)
        label.pack()
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        label.pack()
        countdown(short_break_sec)
    else:
        label["text"] = "Work"
        label.pack()
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes, secs = divmod(count, 60)
    time_format = '{:02d}:{:02d}'.format(minutes, secs)
    canvas.itemconfig(timer_text, text=time_format)
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_time()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

window.title("Pomodoro Project")
label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label.pack()
bg = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 114, image=bg)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.pack()
button_start = Button(text="Start", highlightthickness=0, command=start_time)
button_start.pack(side="left")
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.pack(side="right")

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.pack(side="bottom")

window.mainloop()
