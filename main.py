import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

def start_timer():
  return()
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

labelA = Label(text="Timer",font=(FONT_NAME,50,"bold"))
labelA.config(bg=YELLOW,fg=GREEN)
labelA.grid(column=2, row=1)

labelB = Label(text="✔",font=(FONT_NAME,20,"bold"))
labelB.config(bg=YELLOW,fg=GREEN)
labelB.grid(column=2, row=5)

button_start = Button(text="start", command=start_timer)
button_start.grid(column=1,row=5)




window.mainloop()