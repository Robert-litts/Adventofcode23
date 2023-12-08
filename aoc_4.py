import re
import math

with open('input4.txt', 'r') as file:
    #Read the file line by line
    lines = file.readlines()

input = []


for line in lines:
    input.append(line.strip())

score = 0
cards_drawn = {}
winning_numbers = {}
round=0
for i in input:
    round+=1
    print('Round' + str(round))

    subset = i.split('|') #split the string at the semi-colon delimiter
    sub_subset = subset[0].split(':')
    cards_drawn = list(filter(None, subset[1].split(' ')))
    cards_drawn = {int(x) for x in cards_drawn}
    winning_numbers=list(filter(None, sub_subset[1].split(' ')))
    winning_numbers={int(x) for x in winning_numbers}
    matches = winning_numbers & cards_drawn
    size = len(matches)
    if size >0:
        score += 2**(len(matches)-1)
        print(score)
    

