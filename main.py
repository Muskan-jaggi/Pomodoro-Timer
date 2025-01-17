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
timer_run = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_run)
    canvas.itemconfig(timer_text, text= "00:00")
    label.config(text="TIMER", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    tick.config(text= "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60

    shortbreak_sec = SHORT_BREAK_MIN * 60
    longbreak_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(longbreak_sec)
        label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)

    elif reps % 2 == 0:
        count_down(shortbreak_sec)
        label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)

    else:
        count_down(work_sec)
        label.config(text="WORK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_run
        timer_run = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        tick.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))

canvas.grid(row=1, column=1)

label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset_button.grid(row=2, column=2)

tick = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
tick.grid(row=3, column=1)

window.mainloop()
