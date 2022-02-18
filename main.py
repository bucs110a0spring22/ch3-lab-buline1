import turtle               #1. import modules
import random

#Part A
window = turtle.Screen() 
window.setup(width=300, height=200)
# 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
## Race 1
michelangelo.speed(1)
leonardo.speed(1)
x = random.randrange(1,101)
y = random.randrange(1,101)
michelangelo.forward(x)
leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## Race 2
for i in range(10):
  x_2 = random.randrange(1,11)
  michelangelo.forward(x_2)
  y_2 = random.randrange(1,11)
  leonardo.forward(y_2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
michelangelo.forward(50)
michelangelo.pendown()
##Triangle
sides = 3
for i in range(sides):
  michelangelo.left(360/sides)
  michelangelo.forward(60)
michelangelo.clear()
##Square
sides = 4
for i in range(sides):
  michelangelo.left(360/sides)
  michelangelo.forward(60)
michelangelo.clear()
##Hexagon
sides = 6
for i in range(sides):
  michelangelo.left(360/sides)
  michelangelo.forward(60)
michelangelo.clear()
##Nonagon
sides = 9
for i in range(sides):
  michelangelo.left(360/sides)
  michelangelo.forward(60)
michelangelo.clear()
##Dodecagon
sides = 12
for i in range(sides):
  michelangelo.left(360/sides)
  michelangelo.forward(60)
michelangelo.clear()
window.exitonclick()