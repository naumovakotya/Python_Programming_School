# Task 2

# The program asks the user for a 9-digit integer number
isbn_number = input('Please, enter the first 9-digit interger number of the ISBN:')
len_isbn_number = len(isbn_number)

# The check that len of number is 9 and this is a number
try:
    if (len_isbn_number == 9) & int(isbn_number):
        # Calcutes the check digit d_10
        sum_isbn = 0
        for i in range(len_isbn_number):
               sum_isbn += int(isbn_number[i]) * (10-i)
        result = 11 - sum_isbn % 11

         # Checks digit can be 10 or 11
        if result == 10:
             last_digit = 'X'
        elif result == 11:
               last_digit = '0'
        else:
            last_digit = str(result)
            isbn_number += last_digit
        print('The resulting ISBN is', isbn_number)
    else:
        # If the user entered not a 9-digit integer number
        print('This is not a 9-digit interger number')
except:
    # If the user entered not a 9-digit integer number
    print('This is not a 9-digit interger number')