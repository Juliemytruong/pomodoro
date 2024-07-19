import tkinter
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

reps=0

# ---------------------------- TIMER RESET ------------------------------- #

def start_timer():
  global reps
  work_sec=WORK_MIN*60
  short_break_sec=SHORT_BREAK_MIN*60
  long_break_sec=LONG_BREAK_MIN*60

  print(work_sec)


  if reps%2!=0:
    print(reps)
    count_down(work_sec)
  elif reps%2==0 and reps%8==0:
    count_down(long_break_sec)
  else:
    count_down(short_break_sec)


def restart_timer():
  return()
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
  display=math.floor(count/60)
  display_sec=count%60

  if display_sec<10:
    display_sec=f"0{display_sec}"

  canvas.itemconfig(timer_text,text=f"{display}:{display_sec}")
  if count>0:
    window.after(1000,count_down,count-1)



# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

labelA = Label(text="Timer",font=(FONT_NAME,50,"bold"))
labelA.config(bg=YELLOW,fg=GREEN)
labelA.grid(column=2, row=1)

labelB = Label(text="✔",font=(FONT_NAME,20,"bold"))
labelB.config(bg=YELLOW,fg=GREEN)
labelB.grid(column=2, row=5)

button_start = Button(text="start", highlightthickness=0,command=start_timer)
button_start.grid(column=1,row=4)

button_end = Button(text="reset", command=restart_timer,highlightthickness=0)
button_end.grid(column=3,row=4)

window.mainloop()