import csv

# functionts for 1-st task
def read_txt(name_file): 
    with open(name_file, 'r') as file:
        data = file.read().lower()
        lst = []
        str = ''
        for el in data:
            if not el.isalpha() and not el == '-':
                if len(str) != 0:
                    lst.append(str)
                lst.append(el)
                str = ''           
            else:
                str += el
        if len(str) != 0:
            lst.append(str)
    return lst

def prepare_data(lst):
    res = lst.copy()
    for x in lst:
        if len(x) == 1:
            if not x[0].isalpha():
                res.remove(x)
    return res

def open_and_prepare_data(name_file_par):
    resul1 = read_txt(name_file_par)
    return prepare_data(resul1)
    
def calculate_occurence(file):
    lst = []
    check_lst = []   
    for word in file:
        if word not in check_lst:
            check_lst.append(word)
            lst.append([word, file.count(word), len(word), len(lst)]) # word | occurence | lenght | index
    return lst 

def cvs_output(lst):
    with open('output.csv', 'w', newline = '') as file:
        writer = csv.DictWriter(file, ['word', 'occurence', 'lenght'])
        writer.writeheader()     
        for x in lst:
            writer.writerow({'word': x[0], 
                        'occurence': x[1],
                        'lenght': x[2]})
            
def compression_txt(f_name,nested_lst):
    file_prepared = read_txt(f_name)
    res = []
    for item in file_prepared:
        if item in nested_lst:
            res.append(nested_lst[-(nested_lst.index(item) + 1)])
        else:
            res.append(item)
    res = ''.join(res)
    with open('Compressed_input.txt', 'w', newline = '') as file:
        file.write(res)
