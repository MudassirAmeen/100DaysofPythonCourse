import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, Quizbrain: QuizBrain):
        self.quiz = Quizbrain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tk.Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=2, row=1)

        self.canvas = tk.Canvas(width=300, height=250,  highlightthickness=0, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Hello world! This is ", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=1, row=2, columnspan= 2, pady=50)

        self.rightImageFile = tk.PhotoImage(file="images/true.png")
        self.rightImage = tk.Button(image=self.rightImageFile, highlightthickness=0, command=self.trueButton)
        self.rightImage.grid(column=1, row=3)

        self.wrongImageFile = tk.PhotoImage(file="images/false.png")
        self.wrongImage = tk.Button(image=self.wrongImageFile, highlightthickness=0, command=self.falseButton)
        self.wrongImage.grid(column=2, row=3)

        self.next_quistion()
        self.window.mainloop()

    def next_quistion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.text =self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=self.text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.rightImage.config(state="disable")
            self.wrongImage.config(state="disable")
    def trueButton(self):
        self.feedback(self.quiz.check_answer("true"))
        
    def falseButton(self):
        self.feedback(self.quiz.check_answer("false"))
    
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_quistion)
    