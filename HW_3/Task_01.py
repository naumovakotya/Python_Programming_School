# Task 01

# libraries
import os
import functions as f

# one str for me (not for task)
os.system('cls' if os.name == 'nt' else 'clear')

try:
    name_file = input('''Please, write a name of the file that you want to open.
This file should be in the same folder that this module and the file format should be txt.
For example, Input.txt
                         
Write here:''')
    
    str = f.open_and_prepare_data(name_file)
    nested_lst = f.calculate_occurence(str)
    nested_lst = sorted(nested_lst, key=lambda x:(-x[1], -x[2], x[3]))
    f.cvs_output(nested_lst)
    f.compression_txt(name_file,[x[0] for x in nested_lst])

except:
    print("File isn't in the same folder or something going wrong")


# "Идеи по улучшению (после получения обратной связи по дз)":
# 1) В calculate_occurence можно было юзать словарь и не париться:)
# 2) Сортировку из этого файла можно было можно зашить в function
# 3) При желании можно перечислить вызываемые функции в импорте,
# тогда не пришлось бы через f каждую вызывать (но не обязательно вовсем)
# 4) Можно было всё зашить в две фунции: для первого и второго файла
