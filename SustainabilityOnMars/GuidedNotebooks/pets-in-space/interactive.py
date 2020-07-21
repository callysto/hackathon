#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 07:44:25 2020

@author: lisacao
"""

#libraries
import random
import pandas
from IPython.display import clear_output

#import data 
pets = pandas.read_csv("pets_from_bootstrap_world.csv")

#colour encoding
Rover = "\033[1;37;40m Rover: \033[0;30m"
__green__ = "\033[1;32m"
__normal__ = "\033[1;0m"
__purple__ = "\033[1;35m"
__blue__ = "\033[1;36m"

# get user's name

def greet(): 
    name = input(Rover + "Heya! I guess we'll be working together from now on! What's your name? ")
    print(Rover, "Nice to meet you, ",name,"!")
    return name
    
def userinfo():
    greet()
    
# positive feedback for correct answers
def correct_answer(): 
    list = ["\033[1;35mNice job!", "\033[1;35mRight on!", "\033[1;35mYou rock!", "\033[1;35mI wish I was this good!", "\033[1;35mWhat a rockstar coder!", "\033[1;35mCorrect!", "\033[1;35mGlad we have you around!", "\033[1;35mThat was great!", "\033[1;35mYou're picking up on this really well!", "\033[1;35mEven Rover is impressed!"]
    nice = print(random.choice(list), __normal__)
    return nice 

################################ CHALLENGE 1
# Question 1 A
def challenge1A():
    print(Rover, "According to the documents, if we want to use the commands we need to bring in a library called \033[1;32mpandas\033[1;0m into the notebook using some code. \033[1;36mTry to fill in the import command.\033[1;0m")
    def Q1A(): 
        ans = str(input("\033[1;32m import \033[1;0m"))
        if ans == "pandas":
            correct_answer()
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
        if ans1 == "pets_from_bootstrap_world.csv" or ans1 == "\"pets_from_bootstrap_world.csv\"": 
            correct_answer()
        else: 
            print(Rover, "Try again. Make sure you spelled everything correctly and includes the file extension")
            Q1B_1()
        clear_output()
        
    def Q1B_2(): 
        ans2 = str(input("The library we want to use that contains the \033[1;32mread_csv\033[1;0m function is: "))
        if ans2 == "pandas":
            correct_answer()
        else: 
            print(Rover, "Try again. Remember it is case sensitive.")
            Q1B_2()
        clear_output()
        
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
    return pandas.read_csv("pets_from_bootstrap_world.csv")

# Question 1 C
def challenge1C():
    ans = str(input("We can also "))
    
    
################################ CHALLENGE 2
    
# Question 2 A
def challenge2A(): 
    codeword = input("\033[1;36m Enter a codeword (also known as a variable name):\n" + Rover + "It can be anything! ")
    value = input("Now, \033[1;36menter a value for the variable\033[1;0m , it can also be anything!\n \033[1;32m" + str(codeword) + " = \033[1;0m")
    
    def Q2A_1():
        code = str(input("Now, \033[1;36menter your codeword again\033[1;0m "))
        if code == str(codeword) :
            print(value)
            correct_answer()
            print(Rover, "Notice how when you entered the variable name, it gave you the value instead? This is handy for saving time by making long pieces of code short!")
        else:
            print(Rover, "Try typing the codeword from above, remember to make sure your spelling and capitalization is the same too. ")
            Q2A_1()
        clear_output()
            
    def Q2A_2(): 
        ans = str(input("Now, let's try assigning the dataset to as a variable!\n\033[1;32m pets =  \033[1;0m"))
        if ans == "pandas.read_csv(\"pets_from_bootstrap_world.csv\")":
            correct_answer() 
            ans2 = input("Now, type \033[1;32mpets\033[1;0m to access the data")
            if ans2 == "pets": 
                pets = pandas.read_csv("pets_from_bootstrap_world.csv") 
                return pets
        else:
            print(Rover, "Try the code from the last question!")
            Q2A_2()
    # execute 
    Q2A_1()
    Q2A_2()
    return 

# Question 2 B
def challenge2b(): 
    print("First, we will need to know what columns are in the data. We can do this by either looking at the dataset again, or use \033[1;32mlist(dataset_variable_name.columns)\033[1;0m")
    def Q2B():
        ans = str(input(" \033[1;36mTry filling in the command: \n \033[1;32mlist\033[1;0m"))
        if ans == "(pets.columns)": 
            correct_answer() 
        else: 
            print(Rover, "Hmm, not quite. Make sure you have the brackets at the end and the right spelling, and include the brackets!\033[1;0m")
            Q2B()
    Q2B()
    return list(pets.columns)
    
# Question 2 C 
def challenge2c():
    print("Now that we have all the column names, let's choose a couple to look at. How about the \033[1;32m'Name'\033[1;0m column?\n \033[1;36mSelect the column using \033[1;32mdataset_variable_name[\"column_name\"]\033[1;0m.")
    def Q2C():
        ans = str(input("\033[1;32mpets\033[1;0m"))
        if ans == "['Name']" or ans == "[\"Name\"]":
            correct_answer()
        else: 
            print(Rover, "Remember, it has to be the exact same spelling and case as in the list. Did you double check to use \033[1;32m[ ]\033[1;0m instead of \033[1;32m( )\033[1;0m?")
            Q2C()
    Q2C()
    return pets['Name']
    
# Question 2 D
def challenge2d():
    print("Now, because all the pet names are unique we should try using another column of data.")
    print(Rover, "Hmm, how about animal types? Or better yet, the number of legs on each animal!")
    def Q2D():
        ans = str(input("\033[1;36mFill in the command to get the unique values for the number of legs in the pets data\n\033[1;32mpetlegs = pets[\"Legs\"]\033[1;0m"))
        if ans == ".unique()": 
            correct_answer()
        else: 
            print(Rover, "Close! Make sure you remember the period and brackets \033[1;32m.\033[1;0munique\033[1;32m()")
            Q2D()
    Q2D()
    petlegs = pets['Legs'].unique()
    return petlegs
    
# Question 2 E
def challenge2e(): 
    print("Based on the output, it seems we have a 3 legged animal! Do you know any reason why that might be?\nLet's try and find out which animals are 3 legged.")
    print("First, we'll need to use a basic operator on the 'Legs' column to find the ones that equal to 3.")
    def Q2E():
        ans = input("\033[1;36mTry filling in the command\n\033[1;32mpets['Legs'] == \033[1;0m")
        if ans == 3: 
            correct_answer()
        else: 
            print(Rover, "Try the number of legs")
        Q2E()
    return pets['Legs'] == 3


