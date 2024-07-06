import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Nutrition and Digestion Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food_types = {
    "carbohydrate": {"shape": "circle", "color": "brown", "message": "Carbohydrates are broken down into glucose and provide energy."},
    "protein": {"shape": "triangle", "color": "red", "message": "Proteins are broken down into amino acids and are used to build and repair tissues."},
    "fat": {"shape": "square", "color": "yellow", "message": "Fats provide energy and help absorb vitamins."},
    "vitamin": {"shape": "classic", "color": "green", "message": "Vitamins support various body functions including immunity and bone health."},
    "mineral": {"shape": "turtle", "color": "blue", "message": "Minerals like calcium and iron are crucial for bones and blood."}
}
current_food_type = random.choice(list(food_types.keys()))
food.shape(food_types[current_food_type]["shape"])
food.color(food_types[current_food_type]["color"])
food.penup()
food.goto(0, 100)

segments = []

# Pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Pen for educational messages
message_pen = turtle.Turtle()
message_pen.speed(0)
message_pen.shape("square")
message_pen.color("white")
message_pen.penup()
message_pen.hideturtle()
message_pen.goto(0, -260)

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

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        message_pen.clear()

    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        current_food_type = random.choice(list(food_types.keys()))
        food.shape(food_types[current_food_type]["shape"])
        food.color(food_types[current_food_type]["color"])
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        message_pen.clear()
        message_pen.write(food_types[current_food_type]["message"], align="center", font=("Courier", 16, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            message_pen.clear()

    time.sleep(delay)

wn.mainloop()
