import pandas as pd
from mobilechelonian import Turtle
import numpy as np
def turtle_data(df):
    '''
    Function to read some basic turtles control data and 
    convert it into actually scooting that little turtle around
    very basic so far. 
    
    TODO other command types? 
    '''
    t = Turtle()
    t.speed(10)
    for index, row in df.iterrows(): 
        t.pencolor(row.color)
        if np.isnan(row.length):
            if row.direction == "left":
                t.left(row.angle)
            elif row.direction == 'right':
                t.right(row.angle)
        elif np.isnan(row.angle):
            if row.direction == "forward":
                t.forward(row.length)
            elif row.direction == "backward":
                t.backward(row.length)