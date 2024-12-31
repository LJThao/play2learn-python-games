"""Math Facts Practice Game"""
# Import modules
import random
import time


def math_game():
    """Start the Math Facts Practice Game"""
    print("Let's start the Math Facts Practice Game!")

    # Choosing an operation
    op = input("Please enter an operation [+, -, x, /]: ").strip()
    while op not in ['+', '-', 'x', '/']:
        print("That is not a correct operation. Please try again [+, -, x, /]: ")
        op = input("Please enter an operation [+, -, x, /]: ").strip()

    # Choosing a number from 1 to 100
    while True:
        try:
            max_num = int(input("Please enter a max number between 1 and 100: "))
            if 1 <= max_num <= 100:
                break
            print("Number isn't between 1 and 100. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Starting the time then initializing the score
    start_time = time.time()
    score = 0

    def get_remaining_time():
        """Returns the remaining time"""
        return 30 - int(time.time() - start_time)

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a // b

    # Operations
    operations = {
        '+': add,
        '-': subtract,
        'x': multiply,
        '/': divide
    }

    while get_remaining_time() > 0:
        # Randomly generate numbers and making sure division is a whole number
        num1, num2 = random.randint(1, max_num), random.randint(1, max_num)
        if op == '/':
            num1 *= num2

        # Calculating the answer then formats the question
        answer = operations[op](num1, num2)
        question = f"{num1} {op} {num2}"

        # Prompt the user until they get the answer right or time runs out
        while get_remaining_time() > 0:
            print(f"\n{question} = ?")
            print(f"You have {get_remaining_time()} seconds left.")
            try:
                user_answer = int(input("Enter an answer: "))
                if user_answer == answer:
                    score += 1
                    print(f"{user_answer} is correct!")
                    break
                # Move on to the next question
                print(f"{user_answer} is not correct. Try again! {question} = ?")
                print(f"You have {get_remaining_time()} seconds left.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Display ending messages based on the outcome
    print("\nTime is up!")
    print("Sorry, you didn't get that answer in on time.")
    print(f"You answered {score} problem(s)!")

    # Play the game again or exit
    if input("Press Enter to play again or any other key to exit: ").strip() == '':
        math_game()


if __name__ == "__main__":
    math_game()
