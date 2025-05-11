for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # debugged incorrect logical "or" operator
        print("FizzBuzz")
    elif number % 3 == 0:                   # debugged incorrect "if" statement
        print("Fizz")
    elif number % 5 == 0:                   # debugged incorrect "if" statement
        print("Buzz")
    else:
        print([number])
