# https://github.com/bmoorefarrell/csci102-wk12-git
# Brant Moore-Farrell
# CSCI 102 - Section B
# Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(user_file):
    with open(user_file) as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]
    return lines

#This takes the first string, goes to the specified index, replaces that index with the second string,
#then adds the rest of the first string (the part after the specified index)
def UpdateString(string_a, string_b, index):
    new_string = string_a[:index] + string_b + string_a[index + 1:]
    return new_string

#counts number of occurrences of user_string in user_list
def FindWordCount(user_list, user_string):
    return user_list.count(user_string)

def ScoreFinder(name_list, score_list, name_request):
    for i in range(len(name_list)):
        if name_list[i] == name_request:
            position = i
            name = name_list[i]
            print('OUTPUT', name, 'got a score of', score_list[position])
    if name_request not in name_list:
        print('OUTPUT player not found')
            
def Union(list_a, list_b):
    return list_a + list_b

def Intersection(first_list, second_list):
    return set(first_list).intersection(second_list)

def NotIn(list_1, list_2):
    list_3 = [i for i in list_1 if i not in list_2]
    return list_3

        
        
