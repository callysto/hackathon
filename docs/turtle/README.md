# Turtle Hackathon

## Introduction

[Turtle graphics](https://en.wikipedia.org/wiki/Turtle_graphics) have been used for learning about programming and computational thinking. We will use them as a fun way to learn about Python programming and Jupyter notebooks.

---

## Turtle Commands

The code you need to run will import the [Turtle drawing code library](https://github.com/takluyver/mobilechelonian) then create a new turtle drawing canvas.

```
from mobilechelonian import Turtle
t = Turtle()
```

Assuming that your turtle is now named `t`, here are the possible commands you can use.

|Command|Description|Example|
|-|-|-|
|`t.speed(integer)`|speed of your turtle, from 1 to 10|`t.speed(10)`|
|`t.right(degrees)`|turn turtle right a certain number of degrees|`t.right(90)`|
|`t.left(degrees)`|turn turtle left a certain number of degrees|`t.left(45)`|
|`t.forward(units)`|move your turtle forward a certain number of pixels|`t.forward(100)`|
|`t.backward(units)`|move your turtle forward a certain number of pixels|`t.backward(20)`|
|`t.penup()`|now your turtle can move without drawing lines|`t.penup()`|
|`t.pendown()`|make your turtle draw lines again|`t.pendown()`|
|`t.pencolor('color')`|color of your turtle’s line using a [color names](https://www.w3schools.com/colors/colors_names.asp)|`t.pencolor('blue')`|
|`t.pencolor('rgb(R, G, B)')`|color of your turtle’s line using red, green, and blue values from 0 to 255|`t.pencolor('rgb(0, 255, 100)')`|
|`t.setposition(x, y)`|move the turtle to a specific position. (0,0) is the top left and (400, 400) is the bottom right|`t.setposition(100, 250)`|
|`t.circle(r, degrees)`|have your turtle draw a piece of a circle of radius r, through some number of degrees|`t.circle(40, 360)`|

For some inspiration, check out [this example](https://github.com/callysto/TMTeachingTurtles/blob/jupyter-turtles-art-contest/turtles-cool-art-demo.ipynb).

---

## Hackathon Challenges

These challenges do not need to be completed in a particular order. Notify a supervisor when you have accomplished one so they can award you points.

Complete the challenges on [the Callysto Hub](https://2i2c.callysto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fhackathon&branch=master&subPath=HackathonNotebooks/Turtles/turtle.ipynb&depth=1).

### Beginner

These challenges are worth 2 points each.

1. draw a red rectangle
1. draw a green triangle
1. draw a blue circle
1. draw a purple pentagon
1. draw a yellow star
1. draw a cyan arrow
1. draw an orange parallelogram
1. draw a magenta hexagon
1. draw a face
1. draw the symbol π

### Intermediate

These challenges are worth 5 points each.

1. draw a pink heart
1. draw a Venn diagram
1. draw a right angle triangle with the RGB color `(205, 133, 63)`
1. draw an equilateral triangle with a perimter of 90 pixels
1. draw a semi-circle with two different colors
1. draw a silver crescent
1. draw [Pac-Man](https://en.wikipedia.org/wiki/Pac-Man)
1. draw a [house](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-house.png)
1. draw a house with a door, a window, and a chimney
1. draw a [simple black flower](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-simple-black-flower.png)
1. draw a [black flower](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-black-flower.png)
1. use [loops](https://www.w3schools.com/python/python_for_loops.asp) in a drawing
1. use [nested loops](https://www.w3schools.com/python/gloss_python_for_nested.asp) in a drawing
1. use [functions](https://www.w3schools.com/python/python_functions.asp) in a drawing
1. draw an emoji

### Advanced

These challenges are worth 15 points each.

1. draw a [pointy coloured flower](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-pointy-flower.png)
1. draw a full [maple leaf](https://github.com/callysto/TMTeachingTurtles/blob/jupyter-turtles-art-contest/turtles-cool-art-demo.ipynb)
1. draw a landscape scene with mutliple colours
1. write your name with a turtle
1. draw a one-octave piano keyboard
1. use a [dataframe to create a turtle drawing](https://github.com/callysto/TMTeachingTurtles/blob/master/TMDataTurtles/turtles-and-data-student.ipynb)
1. create a function that accepts an integer parameter and draws a shape with that many sides
1. create a 15-second promo video introducing Python turtles to people your age
1. write a note about your experiences today to share with your grownups or friends
1. **near the end of the day, complete this anonymous hackathon feedback [survey](https://docs.google.com/forms/d/e/1FAIpQLSd0Ih8x_dHS1FDfw4WYwcZAirwagfkbqoB9_WO1XoV5WqAi3Q/viewform?usp=pp_url&entry.1760849759=2028-12-31&entry.975699384=Turtles,+AB).**

## Submit
Use [this form](https://docs.google.com/forms/d/e/1FAIpQLSeEc161W1hYPaR1g1mNH0Y0QGhO1VsygXSxwCqhLkAzusiJ8w/viewform?usp=sf_link) to submit your:
- Team name
- Team members
- Answers to the reflection questions:
    1. What are two things you've learned so far?
    1. What has been your favourite part of this activity?
    1. Are there other things you would like to create with Python turtles?
    
Note: **If you do not submit answers to the reflection questions, your team will not be considered for any prizes**