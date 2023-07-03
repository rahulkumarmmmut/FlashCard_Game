from tkinter import *
from tkinter import messagebox

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn ={}
try:
    data = pd.read_csv(r"word_I_need_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv(r"french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    #print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def isknown():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("word_I_need_to_learn.csv", index=False)
    next_card()





window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="card_back.png")
card_front_img = PhotoImage(file="card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word  = canvas.create_text(400, 250, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0, command= isknown)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command = next_card)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()
