from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
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

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    time_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="Break", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="Break", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=PINK)
    else:
        count_down(work_sec)
        time_label.config(text="Work", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    #Getting minutes and rounding to floor number
    count_min = math.floor(count/60)
    #Getting the seconds
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#highlightthickness needed because of img border showing up
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Week_4/Day_28/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=2)

#Time Label
time_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
time_label.grid(column=1,row=1)

#Check Mark Label
#text="✔",
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=4)

#Start Button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

#Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)


window.mainloop()