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

    global num1, num2, answer, count

    if count < totalQuestions:
        # finds a random number between 1 and 20 for num1 and num2
        num1 = random.randint(1,20) 
        num2 = random.randint(1,20)
        # the correct answer is num1*num2 which is stored as answer
        answer = num1*num2

    else:
        # will need to end somehow
        end_quiz()

def check_answer():
    global score, count

    try:
        user_answer = int(answerField.get())
        if user_answer == num2:
            resultLabel.config(text="Correct!", fg="green")
            score += 1
        else:
            resultLabel.config(text=f"Wrong! The correct answer was {num2}", fg="red")

        scoreLabel.config(text=f"Score: {score}")
        question_count += 1
        window.after(2000, questions)

    except ValueError:
        resultLabel.config(text="Please enter a valid number.", fg="red")

def end_quiz():
    questionLabel.config(text="Quiz Complete!")
    answerField.pack_forget()
    submitButton.pack_forget()
    resultLabel.config(text=f"Your final score is {score}/{total_questions}", fg="blue")


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

resultLabel = tk.Label(window, text="", font=("Arial", 14))
resultLabel.pack(pady=10)

answerField = tk.Entry(window, font=("Arial", 14))
answerField.pack(pady=10)
answerField.bind("<Return>", lambda event: check_answer())

# starts with questions
questions()

# runs the game
window.mainloop()