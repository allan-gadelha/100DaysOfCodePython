import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Brazil State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

score = 0

df = pd.read_csv("50_states.csv")
all_states = df.state.tolist()
print(all_states)


while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        score += 1