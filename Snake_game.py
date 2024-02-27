# Made by Hasan Alp Doyduk and Ismail Akbas

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # screen update timer

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("light green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("pink")
food.penup()

# Tail
tail = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("turtle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Health bars
health_1 = turtle.Turtle()
health_1.speed(0)
health_1.shape("square")
health_1.color("red")
health_1.penup()
health_1.goto(-80, -260)
health_2 = turtle.Turtle()
health_2.speed(0)
health_2.shape("square")
health_2.color("red")
health_2.penup()
health_2.goto(-60, -260)
health_3 = turtle.Turtle()
health_3.speed(0)
health_3.shape("square")
health_3.color("red")
health_3.penup()
health_3.goto(-40, -260)
health_4 = turtle.Turtle()
health_4.speed(0)
health_4.shape("square")
health_4.color("red")
health_4.penup()
health_4.goto(-20, -260)
health_5 = turtle.Turtle()
health_5.speed(0)
health_5.shape("square")
health_5.color("red")
health_5.penup()
health_5.goto(0, -260)
health_6 = turtle.Turtle()
health_6.speed(0)
health_6.shape("square")
health_6.color("red")
health_6.penup()
health_6.goto(20, -260)
health_7 = turtle.Turtle()
health_7.speed(0)
health_7.shape("square")
health_7.color("red")
health_7.penup()
health_7.goto(40, -260)
health_8 = turtle.Turtle()
health_8.speed(0)
health_8.shape("square")
health_8.color("red")
health_8.penup()
health_8.goto(60, -260)
health_9 = turtle.Turtle()
health_9.speed(0)
health_9.shape("square")
health_9.color("red")
health_9.penup()
health_9.goto(80, -260)

health_bar = [health_1, health_2, health_3, health_4, health_5, health_6, health_7, health_8, health_9]


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Health bar action **********************************************************************
if len(health_bar) == 0:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Resetting the tail
    for j in tail:
        j.goto(1000, 1000)

    tail.clear()

    # Reset score
    score = 0

    # Resetting the delay
    delay = 0.1
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Resetting the food's coordinates
    a = random.randint(-290, 290)
    b = random.randint(-290, 250)
    food.goto(a, b)
else:
    for i in range(len(health_bar)):
        time.sleep(delay * 5)
        health_bar.pop()
        death = turtle.Turtle()
        death.speed(0)
        death.shape("square")
        death.color("gray")
        death.penup()
        death.goto(80 - (i * 20), -260)

# Main
while True:
    wn.update()

    # Borders ****************************************************************************
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Resetting the tail
        for j in tail:
            j.goto(1000, 1000)

        tail.clear()

        # Reset score
        score = 0

        # Resetting the delay
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Resetting the food's coordinates
        a = random.randint(-290, 290)
        b = random.randint(-290, 250)
        food.goto(a, b)

    # Eat **********************************************************************************
    if head.distance(food) < 20:
        # Random spotting food
        x = random.randint(-290, 290)
        y = random.randint(-290, 250)
        food.goto(x, y)
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("dark green")
        new_tail.penup()
        tail.append(new_tail)

        # Delay shorting
        delay -= 0.001

        # Update score
        score += 1
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Tail-tail follow ***********************************************************************
    for index in range(len(tail) - 1, 0, -1):
        x = tail[index - 1].xcor()
        y = tail[index - 1].ycor()
        tail[index].goto(x, y)

    # Tail-head follow ***********************************************************************
    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x, y)

    move()

    # Eating itself ***************************************************************************
    for i in tail:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Resetting the tail
            for j in tail:
                j.goto(1000, 1000)

            tail.clear()

            # Reset score
            score = 0

            # Resetting the delay
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

            # Resetting the food's coordinates
            a = random.randint(-290, 290)
            b = random.randint(-290, 250)
            food.goto(a, b)

    time.sleep(delay)
