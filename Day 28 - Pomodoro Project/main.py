# Day 28
# Pomodoro Project

import tkinter as tk
import math, time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global rep

    window.after_cancel(timer)
    Timer_Label.config(text="TIMER")
    canvas.itemconfig(time_canvas, text=f"00:00")
    check_mark.config(text="")
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if rep in [0, 2, 4, 6]:
        Timer_Label.config(text="WORK")
        count_down(work_time)
        print("work")
    elif rep in [1, 3, 5]:
        Timer_Label.config(text="BREAK", fg=PINK)
        count_down(short_break_time)
        print("short")
    elif rep == 7:
        Timer_Label.config(text="BREAK", fg=RED)
        count_down(long_break_time)
        print("long")
    rep += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global rep,checkmark, timer

    count_down_min = math.floor(count / 60)
    count_down_sec = count % 60
    if count_down_min < 10:
        count_down_min = f"0{count_down_min}"
    if count_down_sec < 10:
        count_down_sec = f"0{count_down_sec}"

    if count_down_sec == 0:
        count_down_sec = "00"
    canvas.itemconfig(time_canvas, text=f"{count_down_min}:{count_down_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if rep in [1, 3, 5, 7]:
            checkmark += "✔"
            check_mark.config(text=checkmark)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# Timer text
Timer_Label = tk.Label(text="TIMER", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
Timer_Label.grid(column = 2, row=1)

# Canvas for image and timer
canvas = tk.Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
image_source = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_source)
time_canvas = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column = 2, row=2)

# Start Timer button
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column = 1, row=3)

# Check mark
checkmark = ""
check_mark = tk.Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column = 2, row=4)

# reset Timer button
reset_button = tk.Button(text="Reset", command=reset)
reset_button.grid(column = 3, row=3)






window.mainloop()
