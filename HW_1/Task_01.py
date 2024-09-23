# Task 1

#The program asks the user for a natural number less than 1_000_000_000
number = input('Please, enter a natural number less then 1_000_000_000: ')

try:
    if 0 < int(number) < 1_000_000_000:
        # If the number correct, we need to find the largest digit of the entered number is displayed.
        largest_digit = '0'
        for digit in number:
            if digit > largest_digit:
                largest_digit = digit
        print ('The largest digit of the entered number is', largest_digit)
    else:
        # If the user entered a number outside the specified range, the program displays the line “ Input error ” and stops.
        print('Input error')
except:
    # If the user entered NOT a number (for example, a string)
    print('Input error')