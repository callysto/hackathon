#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 07:44:25 2020

@author: lisacao
"""

#libraries
import random
import pandas as pandas
from IPython.display import clear_output

#import data 
pets = pandas.read_csv("pets_from_bootstrap_world.csv")

################################ TEXT ENCODING

def rover(text): 
    rvr = "\033[1;37;40m 🐶 Rover: \033[1;0m" + text + "\033[1;0m"
    return rvr

def task(text, check = False): 
    if check == True:
        blu = "\033[1;36m" + "✅ " + text + "\033[1;0m"
        return blu
    else:
        blu = "\033[1;36m" + text + "\033[1;0m"
        return blu

def bedazzle(text): 
     sparkle = ["✨ ", "🌟 ", "🎉 ", "🥳 ", "🤩 ", "🎊 ", "🚀 ", "😎 "]
     prl = "\033[1;35m" + random.choice(sparkle) + text + "\033[1;0m"
     return prl
   
def normal(text): 
     nrl = "\033[1;0m" + text + "\033[1;0m"
     return nrl
 
def code(text): 
     grn = "\033[1;32m" + text + "\033[1;0m"
     return grn
 
def tryagain(text, exclaim = True):
    if exclaim == False:
        red = "\033[1;31m" + text + "\033[1;0m"
        return red
    else:
        red = "\033[1;31m" + "❗️ " + text + "\033[1;0m"
        return red

# positive feedback for correct answers
def correct_answer(): 
    compliment = ["Amazing work!", "Nice job!", "Right on!", "You rock!", "I wish I was this good!", "What a rockstar coder!", "Correct!", "Glad we have you around!", "That was great!", "You're picking up on this really well!", "Even Rover is impressed!"]
    nice = print(bedazzle(random.choice(compliment)))
    return nice 

################################ GREETING

# get user's name
def greet():
    name = input(rover("Heya! I guess we'll be working together from now on! What's your name? "))
    print(rover("Nice to meet you, "),name,"!")
    return name
    
def userinfo():
    greet()

################################ CHALLENGE 1
# Question 1 A
def challenge1a():
    print(rover("According to the documents, if we want to use the commands we need to bring in a library called"), code("pandas"), normal("into the notebook using some code.\n"), task("Try to fill in the", check = True), code("import"), task("command."))
    def Q1A(): 
        ans = str(input(code("import ")))
        if ans == "pandas":
            correct_answer()
        else:
            print(tryagain("Hmm.. not quite. Try"), code("pandas"))
            Q1A()
    Q1A()
    return 

# Question 1 B
def challenge1b(): 
    print(task("Answer the questions correctly to check your understanding.\n", check = True))
    
    def Q1B_1():
        ans1 = str(input(rover("The file we want to use the ") + code("read_csv() ") + normal("function on is: ")))
        if ans1 == "pets_from_bootstrap_world.csv" or ans1 == "\"pets_from_bootstrap_world.csv\"": 
            correct_answer()
        else: 
            print(tryagain("Try again. Make sure you spelled everything correctly and includes the file extension"))
            Q1B_1()
        clear_output(wait = True)
        
    def Q1B_2(): 
        ans2 = str(input(rover("The library we want to use that contains the ")  + code("read_csv() ")  + normal("function is: ")))
        if ans2 == "pandas":
            correct_answer()
        else: 
            print(tryagain("Try again. Remember it is case sensitive."))
            Q1B_2()
        clear_output(wait = True)
        
    def Q1B_3(): 
        ans3 = str(input(task("Try writing code to access the Pets Archives from Earth: ", check = True)))
        if ans3 == "pandas.read_csv(\"pets_from_bootstrap_world.csv\")":
            correct_answer()
        else:
            print(tryagain("Hmm, not quite. Try following the format"), code("library.function(\"file.csv\")"), tryagain("or double check your spelling.", exclaim = False))
            Q1B_3()
    Q1B_1()
    Q1B_2()
    Q1B_3()
    return pandas.read_csv("pets_from_bootstrap_world.csv")

# Question 1 C
def challenge1c(): 
    codeword = input(task("Enter a codeword (also known as a variable name):\n", check = True) + rover("It can be anything! "))
    value = input(task("Now, enter a value for the variable, it can also be anything!\n ", check = True) + code(str(codeword)) + code(" = "))
    pets = pandas.read_csv("pets_from_bootstrap_world.csv") 
    def Q1C_1():
        code = str(input(task("Now, enter your codeword again ", check = True)))
        if code == str(codeword) :
            print(value)
            correct_answer()
            print(rover("Notice how when you entered the variable name, it gave you the value instead? This is handy for saving time by making long pieces of code short!"))
        else:
            print(tryagain("Try typing the codeword from above, remember to make sure your spelling and capitalization is the same too. "))
            Q1C_1()
        clear_output(wait = True)
            
    def Q1C_2(): 
        ans = str(input(task("Now, let's try assigning the dataset to as a variable!\n", check = True) + code("pets =  ")))
        if ans == "pandas.read_csv(\"pets_from_bootstrap_world.csv\")" or ans == "pandas.read_csv('pets_from_bootstrap_world.csv')":
            correct_answer() 
        else:
            print(tryagain("Try the code from the last question!", exclaim = True))
            Q1C_2()
        clear_output(wait = True)
        
    def Q1C_3(): 
        ans2 = input(task("Now, type ", check = True) + code("pets ") + task(" to access the data\n"))
        if ans2 == "pets": 
            correct_answer()
        else:
            print(tryagain("Try typing ", exclaim = True) + code("pets "))
            Q1C_3()
    # execute 
    Q1C_1()
    Q1C_2()
    Q1C_3()
    return pets
    
    
################################ CHALLENGE 2
    
# Question 2 A
def challenge2a():
    def Q2A_1():
        ans = str(input(rover("If I only wanted to see the top of the dataset I would write: \n") + code("pets")))
        if ans == ".head()": 
            correct_answer() 
        else: 
            print(tryagain("Not quite, try "), code(".head()"))
            Q2A_1()
        clear_output(wait = True)
        return pets.head()
    def Q2A_2(): 
        ans2 = str(input(rover("If I only wanted to see the bottom of a dataset I would write: \n") + code("pets")))
        if ans2 == ".tail()": 
            correct_answer()
        else: 
             print(tryagain("Not quite, try"), code(".tail()"))  
             Q2A_2()
        return pets.tail()       
    print(Q2A_1())
    print(Q2A_2())
    
    
# Question 2 B
def challenge2b(): 
    print(rover("First, we will need to know what columns are in the data. We can do this by either looking at the dataset again, or use "), code("dataset_variable_name.columns"))
    def Q2B():
        ans = str(input(task("Try filling in the command: \n", check = True) + code("list")))
        if ans == "pets.columns": 
            correct_answer() 
        else: 
            print(tryagain("Hmm, not quite. Make sure you have the right spelling!"))
            Q2B()
    Q2B()
    return list(pets.columns)
    
# Question 2 C 
def challenge2c():
    print(rover("Now that we have all the column names, let's choose a couple to look at. How about the "), code("'Name' "), normal("column?\n"), task("Select the column using ", check = True), code("dataset_variable_name[\"column_name\"]"))
    def Q2C():
        ans = str(input(code("pets")))
        if ans == "['Name']" or ans == "[\"Name\"]":
            correct_answer()
        else: 
            print(rover("Remember, it has to be the exact same spelling and case as in the list. Did you double check to use "), code("[ ] "), normal("instead of "), code("( )"), normal("?"))
            Q2C()
    Q2C()
    return pets['Name']
    
################################ CHALLENGE 3

# plot example 
def challengeplotall(): 
    
    

# Question 3 A
def challenge3a():
    print(rover("Now, because all the pet names are unique we should try using another column of data.\nHmm, how about animal types? Or better yet, the number of legs on each animal!"))
    def Q3A():
        ans = str(input(task("Fill in the command to get the unique values for the number of legs in the pets data\n", check = True) + code("petlegs = pets[\"Legs\"]")))
        if ans == ".unique()": 
            correct_answer()
        else: 
            print(tryagain("Close! Make sure you remember the period and brackets. Use "), code("dataset['columnname'].unique()"))
            Q3A()
    Q3A()
    petlegs = pets['Legs'].unique()
    return petlegs
    
# Question 3 B
def challenge3b(): 
    print(rover("Based on the last challenge, it seems we have a 3 legged animal! Do you know any reason why that might be?\nLet's try and find out which animals are 3 legged."))
    print(rover("First, we'll need to use a basic operator on the 'Legs' column to find the ones that equal to 3."))
    def Q3B():
        ans = str(input(task("Try filling in the command\n", check = True) + code("pets['Legs'] == ")))
        if ans == "3": 
            correct_answer()
        else: 
            print(tryagain("Try the number of legs"))
            Q3B()
        return pets['Legs'] == 3
    print(Q3B())
  
# Question 3 C
def challenge3c():
    print(rover("Looks like there's only one row that returns "), code("True "), normal("can you use "), code(".loc"), normal(" to find out more?"))
    def Q3B(): 
        ans = str(input(task("Fill in the command:\n", check = True) + code("pets")))
        if ans == ".loc[19]":
            correct_answer()
            return print(pets.loc[19])
        elif ans == ".loc[[19]]":
            correct_answer()
            return print(pets.loc[[19]])
        else:
            print(tryagain("Try using "), code(".loc[rownumber]"), tryagain(" or ", exclaim = False), code(".loc[[rownumber]]"), tryagain(", the second outputs as a row!", exclaim = False))
            Q3B()
    print(Q3B())
    
def challenge3d(): 
    print(rover("Good work!! Let's try to do some other examples. Since I'm a dog that's over 100lbs, I want to see if there are any other dogs like me! Can you try and find out?"))
    def Q3D_1(): 
        ans1 = str(input(task("Try to find the all the dogs with the first operator below!\n", check = True) + code("pets.loc")))
        if ans1 == "[(pets[\"Species\"] == \"dog\")]" or ans1 == "[(pets['Species'] == 'dog')]":
            correct_answer()
            print(pets.loc[(pets["Species"] == "dog")])
        else:
            print(tryagain("Very close! Why don't you try "), code("[(pets[\"column_name\"] == \"filter_word\")] "), tryagain("where the column is 'Species' and filter is 'dog'? Remember: capitalization matters!", exclaim = False))
            Q3D_1()
        clear_output(wait = True)
 
    def Q3D_2(): 
        ans2 = str(input(task("Awesome! Now try to write an operator that can find all animals over 100 pounds!\n", check = True) + code("pets.loc")))
        if ans2 == "[(pets['Weight (lbs)'] > 100)]" or ans2 == "[(pets[\"Weight (lbs)\"] > 100)]":
            correct_answer()
            print(pets.loc[(pets["Weight (lbs)"] > 100)])
        else: 
            print(tryagain("Try "), code("[(pets[\"column_name\"] > number_of_lbs)] "), tryagain("where the column is 'Weight (lbs)' and number of lbs is 100 Remember: spelling and spaces matter!", exclaim = False))
            Q3D_2()
        clear_output(wait = True)
  
    def Q3D_3(): 
        print(rover("Wow! You're really good. I always had trouble with doing that stuff. How about we try to do both at once? I think the format was "), code("pets.loc[(operator1) & (operator2)]"))
        def Q3D_3A():
            ans3 = str(input(task("Try to combine the two operators you wrote previously. Remember to always have matching brackets!\n", check = True) + code("pets.loc")))
            #alternatively can potentially use regex to parse this 
            if ans3 == "[(pets[\"Weight (lbs)\"] > 100) & (pets[\"Species\"] == \"dog\")]" or ans3 == "[(pets['Weight (lbs)'] > 100) & (pets['Species'] == 'dog')]": 
                correct_answer()
                return pets.loc[(pets['Weight (lbs)'] > 100) & (pets['Species'] == 'dog')]
            else:
                print(tryagain("This one is definitely tricky! Try seeing what you may have missed by comparing your answer to this: \n"), code("pets.loc[(pets['Weight (lbs)'] > 100) & (pets['Species'] == 'dog')] "))
                Q3D_3A()
        Q3D_3A()
    Q3D_1()
    Q3D_2()
    Q3D_3()
    return pets.loc[(pets['Weight (lbs)'] > 100) & (pets['Species'] == 'dog')]
    
################################ CHALLENGE 4
    
def challenge4a():
    print(rover("I wonder how many pets are planning to be adopted soon! Should that be considered?"))
    print(task("Try filling in the command to sort values by", check = True), code("'Time to Adoption (weeks)'"))
    def Q4A(): 
        ans = str(input(code("pets")))
        if ans == ".sort_values(by='Time to Adoption (weeks)')" or ans == ".sort_values(by=\"Time to Adoption (weeks)\")":
            correct_answer()
        else: 
            print(rover("Better than I could have done!\n"), tryagain("Try .sort_values(by='Time to Adoption (weeks)')"))
            Q4A()
    Q4A()
    return pets.sort_values(by = 'Time to Adoption (weeks)')

def challenge4b():
    print(rover(""))

              
