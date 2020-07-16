#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 07:44:25 2020

@author: lisacao
"""

import random

#colour encoding
Rover = "\033[1;37;40m Rover: \033[1;0m"
__green__ = "\033[1;32m"
__normal__ = "\033[1;0m"
__purple__ = "\033[1;35m"
__blue__ = "\033[1;36m"

# get user's name
def userinfo():
    name = input("\033[1;37;40m Rover: \033[1;0m Heya! I guess we'll be working together from now on! What's your name? ")
    print(Rover, "Nice to meet you, ",name,"!")
    
# positive feedback for correct answers
def correct_answer(): 
    list = ["\033[1;35mNice job!", "\033[1;35mRight on!", "\033[1;35mYou rock!", "\033[1;35mI wish I was this good!", "\033[1;35mWhat a rockstar coder!", "\033[1;35mCorrect!", "\033[1;35mGlad we have you around!", "\033[1;35mThat was great!", "\033[1;35mYou're picking up on this really well!", "\033[1;35mEven Rover is impressed!"]
    nice = print(random.choice(list))
    return nice 

################################ CHALLENGE 1
# Question 1 A
def challenge1A():
    print(Rover, "According to the documents, if we want to use the commands we need to bring in a library called \033[1;32mpandas\033[1;0m into the notebook using some code. \033[1;36mTry to fill in the import command.\033[1;0m")
    def Q1A(): 
        ans = str(input("\033[1;32m import \033[1;0m"))
        if ans == "pandas":
            correct_answer()
            print(Rover, "Now, \033[1;36m type the command in the empty cell below.\033[1;0mWe also need the libraries \033[1;32mnumpy\033[1;0m and \033[1;32mmatplotlib\033[1;0m, can you import them as well?. Each library will need its own import line. Remember to \033[1;36mhit the run button above after you're done!\033[1;0m")
        else:
            print(Rover, "Hmm.. not quite. Try \033[1;32mpandas\033[1;0m")
            Q1A()
    Q1A()
    return 

# Question 1 B
def challenge1B(): 
    print("\033[1;36mAnswer the questions correctly to check your understanding.\033[1;0m\n")
    def Q1B_1():
        ans1 = str(input("The file we want to use the \033[1;32mread_csv\033[1;0m function on is: "))
        if ans1 == "pets_from_bootstrap_world.csv": 
            correct_answer()
        else: 
            print(Rover, "Try again. Make sure you spelled everything correctly and includes the file extension")
            Q1B_1()
    def Q1B_2(): 
        ans2 = str(input("The library we want to use that contains the \033[1;32mread_csv\033[1;0m function is: "))
        if ans2 == "pandas":
            correct_answer()
        else: 
            print(Rover, "Try again. Remember it is case sensitive.")
            Q1B_2()
    def Q1B_3(): 
        ans3 = str(input("\033[1;36mIf I wanted to write code to access the Pets Archives from Earth, I would write:\033[1;0m "))
        if ans3 == "pandas.read_csv(\"pets_from_bootstrap_world.csv\")":
            correct_answer()
        else:
            print(Rover, "Hmm, not quite. Try following the format \033[1;32mlibrary.function(\"file.csv\")\033[1;0m, or double check your spelling.")
            Q1B_3()
    Q1B_1()
    Q1B_2()
    Q1B_3()
    print(Rover, "Now, \033[1;36mtype that exact code in the empty cell below and run it\033[1;0m, just like before")
    return
    
################################ CHALLENGE 2
# Question 2 A
def challenge2A(): 
    codeword = input("\033[1;36m Enter a codeword (also known as a variable name):\n" + Rover + "It can be anything! ")
    value = input("Now, \033[1;36menter a value for the variable\033[1;0m , it can also be anything!\n \033[1;32m" + str(codeword) + " = \033[1;0m")
    def Q2A():
        code = str(input("Now, \033[1;36menter your codeword again\033[1;0m "))
        if code == str(codeword) :
            print(value)
            correct_answer()
            print(Rover, "Notice how when you entered the variable name, it gave you the value instead? This is handy for saving time writing long pieces of code each time")
        else:
            print(Rover, "Try typing the codeword from above, remember to make sure your spelling and capitalization is the same too. ")
            Q2A()
    Q2A()

# Question 2 B
def challenge2b(): 
    print("First, we will need to know what columns are in the data. We can do this by either looking at the dataset again, or use \033[1;32mdataset_variable_name.columns()\033[1;0m")
    def Q2B():
        ans = str(input(" \033[1;36mTry filling in the command: \n \033[1;32mpets.\033[1;0m"))
        if ans == "columns()": 
            correct_answer() 
        else: 
            print(Rover, "Hmm, not quite. Make sure you have the brackets at the end and the right spelling")
            Q2B()
    Q2B()
    print("\033[1;0mFantastic! Now type \033[1;32mpets.columns()\033[1;0m in the cell below and run it.")