from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="win race? Enter a color:")
colors = ["red", "orange", "yello", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_tutles = []
for turtle_index in range(6):
  tim = Turtle(shape="turtle")
  tim.color(colors[turtle_index])
  tim.penup()
  tim.goto(x=-230, y=y_position[turtle_index])
  all_tutles.append(tim)

if user_bet:
  is_race_on =True

while is_race_on:
  
  for turtle in all_tutles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print("good")
      else:
        print("lose")
      
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)




screen.exitonclick()