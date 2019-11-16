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
