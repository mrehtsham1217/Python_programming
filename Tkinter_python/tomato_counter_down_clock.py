"""
 python is strongly dynamically typed language because you
 can change type whenever you want
 thing = "Python language"
 thng = 1217
 print(thing)
 ---------Other languages java c++ -------->
 String thing;
 thing = "Machine learning"
 thing = 1217
 system.out.println(thing)
"""


from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

window = Tk()
window.title("Pomodoro counter clock")
window.config(padx=100, pady=50, bg=YELLOW)
# creating label title
title_label = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)
# creating a clock counter


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after("1000", count_down, count-1)
        # window.after is used in GUI for timer
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks = "✔️"
        check_marks.config(text=marks)


def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="✔️")


# creating convas for image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=("courier", 35, "bold"))
# count_down(5)
canvas.grid(column=1, row=1)
# Creating start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
# creating tick emoji
check_marks = Label()
check_marks.grid(column=1, row=3)
# creating reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
window.mainloop()
