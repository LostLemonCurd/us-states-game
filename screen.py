import turtle
import time


class Screen:
    def __init__(self, title, image):
        self.screen = turtle.Screen()
        self.screen.title(title)
        self.screen.addshape(image)
        turtle.shape(image)

        self.welcome_turtle = turtle.Turtle()
        self.welcome_turtle.hideturtle()

        self.message_turtle = turtle.Turtle()
        self.message_turtle.hideturtle()

        self.score_turtle = turtle.Turtle()
        self.score_turtle.hideturtle()

        self.state_turtle = turtle.Turtle()
        self.state_turtle.hideturtle()

        self.timer_turtle = turtle.Turtle()
        self.timer_turtle.hideturtle()

    def ask_input(self, title, user_input):
        return self.screen.textinput(title, user_input)

    def display_message(self, message, color="black"):
        self.message_turtle.clear()
        self.message_turtle.penup()
        self.message_turtle.hideturtle()
        self.message_turtle.goto(0, 260)
        self.message_turtle.color(color)
        self.message_turtle.write(
            message, align="center", font=("Poppins", 20, "normal")
        )

    def display_score(self, score, total_score):
        self.score_turtle.clear()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(0, -280)
        self.score_turtle.write(
            f"Score: {score} / {total_score}",
            align="center",
            font=("Poppins", 18, "normal"),
        )

    def display_timer(self, timer):
        self.timer_turtle.clear()
        self.timer_turtle.penup()
        self.timer_turtle.hideturtle()
        self.timer_turtle.goto(0, -300)
        self.timer_turtle.write(
            f"Time: {timer} seconds",
            align="center",
            font=("Poppins", 18, "normal"),
        )

    def display_welcome_message(self, message):
        self.welcome_turtle.clear()
        self.welcome_turtle.penup()
        self.welcome_turtle.hideturtle()
        self.welcome_turtle.goto(0, 290)
        self.welcome_turtle.color("darkmagenta")
        self.welcome_turtle.write(
            message, align="center", font=("Poppins", 24, "normal")
        )

    def place_state_on_map(self, state, x, y):
        self.state_turtle.penup()
        self.state_turtle.hideturtle()
        self.state_turtle.goto(x, y)
        self.state_turtle.write(state, align="center")