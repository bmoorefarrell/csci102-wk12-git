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
