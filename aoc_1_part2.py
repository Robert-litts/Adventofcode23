import re

with open('input.txt', 'r') as file:
    #Read the file line by line
    lines = file.readlines()

#store all input into 'input'
input = []
for line in lines:
    input.append(line.strip())



word_dict = {"one": "o1e", "two": "t2o", "three": "th3ree", "four": "fo4r", "five": "fi5e", "six": "s6x", "seven": "se7en", "eight": "ei8ht", "nine": "n9ne"}
#Word Dictionary to find & replace string "words" with numbers

#input = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen'] #Test Input

score = 0 #Initialize score
count = -1 #initialize counter for iterating thru input

for i in input:
    count +=1

    #Find & Replace each word found in the dict from the input
    for key, value in word_dict.items(): 
        i = i.replace(key, value)
    input[count] = i

    #Use Same Algorithm from Part 1 to find leftmost and rightmost numbers & join together
    value = ''

    #Look through each letter & check if it is a number
    for letter in i:
        #If it is a number, add the letter to value
        if letter.isnumeric() == True:
            value += letter

    #find how many letters are stored in value
    size = len(value)

    #If there is only one letter (Meaning only 1 number found)
    if size == 1:
        #Duplicate the value, per the instructions
        value += value[0] 

    #If there is more than one letter (meaning more than 1 number found)   
    elif size >2:
        #Take the first and last values, discrad the rest
        value = value[0] + value[size-1]

    #print(value) #Print value for debugging
    
    score += int(value) #Add the value to the overall score


print("final score is " + str(score))





