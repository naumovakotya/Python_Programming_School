# Task 3

def search_miss_element(lst):
    lst.sort()
    sum_theory = (lst[0] + lst[-1]) * (len(lst)+1) /2

    sum_real = 0
    for e in lst:
        sum_real += e # or function sum()
       
    
    # Rounding because of inaccuracy
    return round(sum_theory - sum_real, 5) 
        
# Tests
test = [[12, 4, 6, 2, 8],
        [9, 7, 1, 5],
        [0.9, -5.5, -0.7, -3.9]]

for t in test:
    print('List:', t)
    print('Answer:', search_miss_element(t))
    print('')