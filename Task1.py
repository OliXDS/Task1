# libraries
import random
import tkinter as tk


# variables

score = 0
answer = 0
count = 0
totalQuestions = 10
num1 = 0
num2 = 0


# functions

def questions():

    if count < totalQuestions:
        # finds a random number between 1 and 20 for num1 and num2
        num1 = random.randint(1,20) 
        num2 = random.randint(1,20)
        # the correct answer is num1*num2 which is stored as answer
        answer = num1*num2

    else:
        # will need to end somehow
        continue


# creates and displays window for game
window = tk.TK() 
# displays title on window
window.title("My Maths Quiz")

submit_button = tk.Button(window, text="Submit", font=("Arial", 14))
submit_button.pack(pady=10)

