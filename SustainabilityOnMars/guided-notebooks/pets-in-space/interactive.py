#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 07:44:25 2020

@author: lisacao
"""

import random

# get user's name
def userinfo():
    name = input("Rover: Nice to meet you! What's your name? ")
    print("Rover: Nice to meet you, ",name,"!")
    
# positive feedback for correct answers
def correct_answer(): 
    list = ["Nice job!", "Right on!", "You rock!", "I wish I was this good!", "What a rockstar coder!", "Correct!", "Glad we have you around!", "That was great!", "You're picking up on this really well!", "Even Rover is impressed!"]
    nice = print(random.choice(list))
    return nice 

# Question 1 A
def challenge1A():
    print("Rover: According to the documents, if we want to use pandas we need to \"bring in\" a library called \"pandas\" into the notebook using some code. Try to fill in the import command.")
    def Q1A(): 
        ans = str(input("import "))
        if ans == "pandas":
            print("Rover: Nice Job!\n\nRover: Now, type the command in the empty cell below. We also need the libraries \"numpy\" and \"matplotlib\", can you import them as well?. Each library will need its own import line. Remember to hit the run button above after you're done! :3")
        else:
            print("Rover: Hmm.. not quite. Try \"pandas\"")
            Q1A()
    Q1A()
    return 

# Question 1 B
def challenge1B(): 
    print("Answer the questions correctly below to check your understanding.\n")
    def Q1B_1():
        ans1 = str(input("The file we want to use the read_csv function on is: "))
        if ans1 == "pets_from_bootstrap_world.csv": 
            correct_answer()
        else: 
            print("Rover: Try again. Make sure you spelled everything correctly and includes the file extension")
            Q1B_1()
    def Q1B_2(): 
        ans2 = str(input("The library we want to use that contains the read_csv function is: "))
        if ans2 == "pandas":
            correct_answer()
        else: 
            print("Rover: Try again. Remember it is case sensitive.")
            Q1B_2()
    def Q1B_3(): 
        ans3 = str(input("If I wanted to write code to access the Pets Archives from Earth, I would write: "))
        if ans3 == "pandas.read_csv(\"pets_from_bootstrap_world.csv\")":
            correct_answer()
        else:
            print("Rover: Hmm, not quite. Try following the format library.function(\"file.csv\"), or double check your spelling.")
            Q1B_3()
    Q1B_1()
    Q1B_2()
    Q1B_3()
    print("\nRover: Now, type that exact code in the empty cell below and run it, just like before")
    return
    

# Question 2 A
def challenge2A(): 
    codeword = input("What would you like your codeword's value to be?\nHint: It can be anything! ")
    def Q2A():
        code = str(input("Now, enter the word \"codeword\" "))
        if code == "codeword":
            print(codeword)
            correct_answer()
        else:
            print("Try typing \"codeword\" ")
            Q2A()
    Q2A()