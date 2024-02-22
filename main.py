import pandas as pd
from quizz_brain import QuizzBrain
from screen import Screen
import turtle
import time

# Load the data
data = pd.read_csv("50_states.csv")

# Create a list of states with their coordinates
statesList = data.to_dict(orient="records")
quizz = QuizzBrain(statesList)
screen = Screen("U.S. States Game", "blank_states_img.gif")

game_start = time.time()
timer = 0
is_timer_active = True


def keep_time():
    global timer
    if is_timer_active:
        timer += 1
        screen.display_timer(timer)
        screen.screen.ontimer(keep_time, 1000)


keep_time()

while quizz.is_there_more_states():
    screen.display_welcome_message("Welcome to guess the U.S. States! 🇺🇸")
    user_answer = screen.ask_input("Guess the state", "Enter a state's name!")
    if user_answer == "exit":
        break
    if user_answer == None:
        break
    answer = quizz.ask_user_input(user_answer)

    if answer:
        screen.display_message(f"Correct! 🚀", "green")
        screen.place_state_on_map(answer[1]["name"], answer[1]["x"], answer[1]["y"])
        screen.display_score(quizz.score, quizz.total_states)
    else:
        screen.display_message(f"Wrong! ❌", "red")
        screen.display_score(quizz.score, quizz.total_states)
print(f"🍾🎊 And it's over! {quizz.display_score()}. 🎊🍾")
is_timer_active = False
screen.display_message(f"🍾🎊 And it's over! {quizz.display_score()}. 🎊🍾", "purple")
turtle.exitonclick()
