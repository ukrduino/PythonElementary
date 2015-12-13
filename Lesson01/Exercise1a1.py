# The program will randomly choose a number within the specified range and
# will wait for the user to input a number.
# If the number is smaller or greater than that chosen by the program,
# the system tells that to the user.
# If the guessed number is correct, then the game is over and the program
# displays the number of iterations taken.

import random

generated_number = random.randint(0, 100)
number_guessed = False
number_of_tries = 0


def check_input(value):
    number = None
    try:
        number = int(value)
    except ValueError:
        print("Its not a valid answer (number in range 0-100).")
    return number


while not number_guessed:
    input_value = raw_input("\nPlease input number in range 0-100\n")
    val = check_input(input_value)
    if val:
        if val in range(0, 100):
            if val < generated_number:
                print "Your number is smaller then my, try again please!"
                number_of_tries += 1
            elif val > generated_number:
                print "Your number is greater then my, try again please!"
                number_of_tries += 1
            elif val == generated_number:
                number_guessed = True
                number_of_tries += 1
                print "Congratulations!!! You guessed number from %i tries" \
                      % number_of_tries
        else:
            print("Your number is not in the range 0-100.")
