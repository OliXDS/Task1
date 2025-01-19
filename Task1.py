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

submitButton = tk.Button(window, text="Submit", font=("Arial", 14))
submitButton.pack(pady=10)

scoreLabel = tk.Label(window, text=f"Score: {score}", font=("Arial", 14))
scoreLabel.pack(pady=10)

questionLabel = tk.Label(window, text="", font=("Arial", 16))
questionLabel.pack(pady=20)

resultLabel = tk.Label(root, text="", font=("Arial", 14))
resultLabel.pack(pady=10)

answerField = tk.Entry(window, font=("Arial", 14))
answerField.pack(pady=10)
