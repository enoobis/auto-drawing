import turtle
import random
from PIL import Image

turtle.setup(500, 500)
turtle.bgcolor("black")
turtle.title("Automatic Drawing")
turtle.speed(0)
turtle.ht()
turtle.penup()

# main function
def lava():
  # Randomly select a start position
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  turtle.goto(x, y)
  turtle.pendown()

  # Set up the shape
  turtle.pensize(5)
  turtle.pencolor("white")
  turtle.fillcolor("black")
  turtle.begin_fill()

  # Draw the shape
  for i in range(30):
    turtle.forward(random.randint(10, 50))
    turtle.left(random.randint(0, 360))
  
  # Close the shape
  turtle.end_fill()

# Call the function repeatedly for overflow effect
while True:
  lava()
  # Save the image
  if len(turtle.getshapes()) >= 500:
    break

# Save the image as a PNG file
turtle.ht()
turtle.getcanvas().postscript(file="image.eps")
img = Image.open("image.eps")
img.save("abstract_lava.png", "png")
