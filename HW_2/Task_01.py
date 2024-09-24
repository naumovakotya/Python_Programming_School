# Task 1

def split_into_two_list(lst):
    n = len(lst)//2
    lst_1 = lst[:len(lst)-n]
    lst_2 = lst[-n:]
    return lst_1, lst_2

# Tests
test = [[1, 2, 3, 4, 5],
        [],
        [1, 2, 3, 4]]

for t in test:
    print('Before:', t)
    print('After:', split_into_two_list(t))
    print('')