import pandas as pd
from quizz_brain import QuizzBrain
from screen import Screen
import turtle
import time

# Load the data
data = pd.read_csv("50_states.csv")

# Create a list of states with their coordinates
statesList = data.to_dict(orient="records")
game_start = time.time()
is_timer_active = True
timer = 0
quizz = QuizzBrain(statesList)
screen = Screen(f"U.S. States Game", "blank_states_img.gif")
total_states = quizz.total_states
score = 0


def keep_time():
    global timer
    if is_timer_active:
        timer += 1
        screen.display_timer(timer, score, total_states)
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

    if answer and answer[0] == True:
        screen.display_message(f"Correct! 🚀", "green")
        screen.place_state_on_map(answer[1]["name"], answer[1]["x"], answer[1]["y"])
        score = quizz.get_score()
    elif answer == "Already Found!":
        screen.display_message(f"Already Found! 🤷🏽‍♂️", "orange")
    else:
        screen.display_message(f"Wrong! ❌", "red")
print(f"🍾🎊 And it's over! {quizz.display_score()}. 🎊🍾")
is_timer_active = False
screen.display_message(f"🍾🎊 And it's over! {quizz.display_score()}. 🎊🍾", "purple")
screen.place_all_states_on_map(statesList)
turtle.exitonclick()
