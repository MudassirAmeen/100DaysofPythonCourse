# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     print(result)

# add(2,2,2,2,3,4,5,6,7,7,8,321,1,1,33,4,5,6)

import tkinter as tk

window = tk.Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=300)


lable_text = tk.Label(text="Mudassir", font=("Times New Roman", 15, "italic"))
lable_text.pack()

Input = tk.Entry()
Input.pack()

def change_text():
    new_text = Input.get()
    lable_text.config(text=new_text)
    # if lable_text["text"] == "Mudassir":
    #     lable_text["text"] = "Mudassir Ameen"
    #     # lable_text.config(text="Mudassir Ameen")
    # else:
    #     lable_text["text"] = "Mudassir"
    #     # lable_text.config(text="Mudassir")


Button = tk.Button(text="Change text", font=("Times New Roman", 10, "italic"), command=change_text)
Button.pack()




window.mainloop()