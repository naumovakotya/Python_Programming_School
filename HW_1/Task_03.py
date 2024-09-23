# Task 3

try:
    # The program asks the user for integers number a
    int_num = int(input('Plese, enter a integer number: '))

    res = 0
    binary_number = ''

    # The program calculates and print its binary representation and quantity of «ones» in it
    while int_num > 0:
        remainder = int_num % 2
        binary_number = str(remainder) + binary_number
        int_num //= 2
        res += remainder
    print('Binary representation:', binary_number)
    print('Quantuty of "ones" in it: ', int(res))
except:
    # If the user entered NOT a integer number
    print('The entered expression is not a interger number')