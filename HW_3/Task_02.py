# Task 02
import os
import json

# one str for me (not for task)
os.system('cls' if os.name == 'nt' else 'clear')

# functions
def sortby_parameter(data, parameter):
    return sorted(data, key=lambda x: x[parameter])

def sortby_login(data):
    return sortby_parameter(data, 'username')

def sortby_id(data):
    return sortby_parameter(data, 'id') 

def groupby_role(data):
    res = {}
    for user in data:
        for role in user['profile']['roles']:
            if role in res:
                res[role].append(user)
            else:
                res[role] = [user]
    return res

def groupby_company(data):
    res = {}
    for user in data:
        com = user['profile']['company']
        if com in res:
            res[com].append(user)
        else:
            res[com] = [user]
    return res

def checking_roles(data, username, role):
    found = [x for x in data if x['username'] == username]
    if len(found) == 0:
        return 'No login matches'
    elif len(found) > 1:
        return 'There are more than 1 eligible users'
    else:
        return f'Role {role} status for {username} is {role in found[0]['profile']['roles']}'
   

# open and check functions
f = open('example.json')
json_data = json.load(f)

# print(f.sortby_login(json_data))
# print(f.sortby_id(json_data))
# print(groupby_role(json_data))
# print(groupby_company(json_data))
# print(checking_roles(json_data, 'darcy23', 'admin'))