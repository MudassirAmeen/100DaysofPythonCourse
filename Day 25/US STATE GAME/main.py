import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
score = 0
screen.addshape("blank_states_img.gif")
screen.setup(width=725, height=491)

turtle.shape("blank_states_img.gif")
allState = data["state"].to_list()

guess_state = []
while len(guess_state)<50:
    answer = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state name?").title()
    
    if answer == "Exit":
        
        miss_states = [state for state in allState if state not in guess_state]

        # miss_states = []
        # for state in allState:
        #     if state not in guess_state:
        #         miss_states.append(state)
        
        new_data = pandas.DataFrame(miss_states)
        new_data.to_csv("new-data.csv")
        break

    if answer in allState:
        guess_state.append(answer)
        correct_answer = data[data.state == answer]
        new_turtle = turtle.Turtle()
        new_x = correct_answer["x"]
        new_y = correct_answer["y"]
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(int(new_x), int(new_y))
        new_turtle.write(answer)
        score += 1
    else:
        pass

turtle.mainloop()

