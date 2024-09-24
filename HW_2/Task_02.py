# Task 2

def del_non_unique_elem(lst):
    dic_uniq = {}

    # searching uniq elements
    for i in lst:
        if i in dic_uniq:
            dic_uniq[i] += 1
        else:
            dic_uniq[i] = 1
    
    res = lst.copy()

    # remove uniq elements
    for j in lst:
        if dic_uniq[j] == 1:
            res.remove(j)

    return res

# Tests
test = [[1, 2, 3, 3, 2],
        [-5, 6, 7, 7, 9, -5, 1, 1],
        [0, 1, 2, 3],
        [0, 0, 0, 0, 0]]

for t in test:
    print('Before:', t)
    print('After:', del_non_unique_elem(t))
    print('')