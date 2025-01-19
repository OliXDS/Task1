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
operation = ""
operations = ["+", "-", "*", "/"] # List of operations to choose from

# functions

def questions():
    """Generates the next question and updates the window (GUI)"""
    global num1, num2, answer, count, operation

    if count < totalQuestions:
        # finds a random number between 1 and 20 for num1 and num2
        num1 = random.randint(1,20) 
        num2 = random.randint(1,20)
        # the correct answer is num1*num2 which is stored as answer
        operation = random.choice(operations)


        # Calculate the answer based on the chosen operation
        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        elif operation == "*":
            answer = num1 * num2
        elif operation == "/":
            num1 = num2 * random.randint(1, 10)  # Ensure division has no remainder
            answer = num1 // num2

        # Update the question label with the new equation
        questionLabel.config(text=f"{num1} {operation} x = {answer}")
        answerField.delete(0, tk.END) # Clear the answer entry field
        resultLabel.config(text="") # Clear the result label

    else:
        # End the quiz if all questions are completed
        end_quiz() 

def check_answer():
    """Checks the user's answer and updates the score and window/GUI"""
    global score, count

    try:
        # Get the user's input as an integer
        user_answer = int(answerField.get())
        if user_answer == num2: # Check if the answer is correct
            resultLabel.config(text="Correct!", fg="green") # Show a success message
            score += 1
        else:
            # Show an error message
            resultLabel.config(text=f"Wrong! The correct answer was {num2}", fg="red")

        # Update the score label
        scoreLabel.config(text=f"Score: {score}")
        count += 1
        # Wait 2 seconds and move to the next question --> could have used time library for this e.g time.sleep()
        window.after(2000, questions)

    except ValueError:
        # when input is invalid
        resultLabel.config(text="Please enter a valid number.", fg="red")

def end_quiz():
    """Displays the final score and ends the quiz"""

    percentage = (score / totalQuestions) * 100 # Calculate the score percentage
    questionLabel.config(text="Quiz Complete!") # Update the question label
    answerField.pack_forget() # Hide the answer entry field
    submitButton.pack_forget() # Hide the submit button
    # display the final score with percentage
    resultLabel.config(text=f"Your final score is {score}/{totalQuestions} ({percentage:.2f}%)", fg="blue")


# creates and displays window for game
window = tk.Tk() 
# displays title on window
window.title("My Maths Quiz")

# Button to submit the answer
submitButton = tk.Button(window, text="Submit", command=check_answer, font=("Arial", 14))
submitButton.pack(pady=10)

# Label to display the current score
scoreLabel = tk.Label(window, text=f"Score: {score}", font=("Arial", 14))
scoreLabel.pack(pady=10)


questionLabel = tk.Label(window, text="", font=("Arial", 16))
questionLabel.pack(pady=20)

# Label to display the result of the answer
resultLabel = tk.Label(window, text="", font=("Arial", 14))
resultLabel.pack(pady=10)

# Answer field for the user's answer
answerField = tk.Entry(window, font=("Arial", 14))
answerField.pack(pady=10)
answerField.bind("<Return>", lambda event: check_answer())

# starts with questions
questions()

# runs the game --> runs the tkinter event loop
window.mainloop()