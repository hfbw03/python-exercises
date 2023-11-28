# ownMultiplicationQuiz.py

import random
import threading
import time

# This function is responsible for getting user input with a specified timeout
def get_user_input(prompt, timeout):
    print(prompt, end='', flush=True)
    user_input = None

    # Defines a function input_thread_func that sets the user_input variable
    # (non-locally) to the value entered by the user using the input() function.
    def input_thread_func():
        nonlocal user_input
        user_input = input()

    # Creates a new thread (input_thread) that will execute the input_thread_func function.
    input_thread = threading.Thread(target=input_thread_func)
    input_thread.start()

    input_thread.join(timeout)  # Wait for the input thread with a timeout
    
    # Interrupt the input thread if it's still alive after the timeout
    if input_thread.is_alive():
        input_thread.join()  # Wait for the input thread to finish
        print("\nTime is up! Moving to the next question.\n")
        return None
    
    return user_input

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    for attempt in range(3):
        # The format of the question with questionNumber + 1
        prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)

        # Get the user's answer within the time limit
        user_answer = get_user_input(prompt, 8)

        if user_answer is None:
            break # Skip the rest of the loop if the time is up

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the user's answer is correct
        if user_answer == num1 * num2:
            print("Correct!\n")
            correctAnswers += 1
            break
        else:
            print("Incorrect!\n")

        # Adding a 1 second delay before moving to the next question
        time.sleep(1)

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

# This one was hard.