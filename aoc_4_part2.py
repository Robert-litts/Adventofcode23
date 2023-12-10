import re
import math

with open('input4.txt', 'r') as file:
    #Read the file line by line
    lines = file.readlines()

input = []
cards={}
x=0
for line in lines:
    x+=1
    input.append(line.strip())
    cards[x] = [1] #create dict with number of copies of each card
    


#print(cards)
score = 0
score_part2 = 0
cards_drawn = {}
winning_numbers = {}
round=0
for q, i in enumerate(input):
    round+=1
    print('Round' + str(round))

    subset = i.split('|') #split the string at the semi-colon delimiter
    sub_subset = subset[0].split(':') #split again at colon

    cards_drawn = list(filter(None, subset[1].split(' '))) #filter by spaces
    cards_drawn = {int(x) for x in cards_drawn} #make the cards ints

    winning_numbers=list(filter(None, sub_subset[1].split(' '))) #remove 'None' from the list
    winning_numbers={int(x) for x in winning_numbers} #extract the winning numbers
    matches = len(winning_numbers & cards_drawn) #calculate the number of matches
    cards[q+1].append(matches)
    
    if matches >0:
        score += 2**(matches-1)
        print(score) #Part 1

    
#Part 2: Look at each card
for q, i in enumerate(input):
    for y in range(q+2, q+2+cards[q+1][1]): #For the range of the next card, to the number of matches on the current card
            cards[y][0]+=cards[q+1][0] #add the number of copies of the current card to the number of copies of the card


#Count the overall number of cards, stored in the dict
for key, value in cards.items():
    score_part2 += value[0]
print(score_part2)
