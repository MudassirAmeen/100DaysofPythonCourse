import tkinter as tk
import pandas,random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv", encoding='utf-8')
except FileNotFoundError:
    Orignal_data = pandas.read_csv("data/french_words.csv")
    data_dict = Orignal_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title_text,text="French", fill="black")
    canvas.itemconfig(word_text,text=current_card["French"], fill="black")
    canvas.itemconfig(background_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text,text="English", fill="white")
    canvas.itemconfig(word_text,text=current_card["English"], fill="white")
    canvas.itemconfig(background_image, image=card_back_image)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create Canvas
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(400, 263, image=card_front_image)

title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(row=1, column=1, columnspan=2)

right_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=2, column=2)

wrong_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=2, column=1)

next_card()
window.mainloop()