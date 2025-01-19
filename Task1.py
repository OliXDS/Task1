# libraries
import random



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
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        answer = num1*num2

    else:
        # will need to end somehow