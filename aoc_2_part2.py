
import re

with open('input_aoc2.txt', 'r') as file:
    #Read the file line by line
    lines = file.readlines()

input = []


for line in lines:
    input.append(line.strip())

## TEST INPUT
#input = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red','Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
score = 0
power = 0
max_red = 12
max_blue = 14
max_green = 13

round=0
for i in input:
    round+=1
    print('Round' + str(round))

    #Initialize minimum numbers of each color needed for Part 2 to calculate power
    min_blue = 0
    min_red = 0
    min_green = 0


    subset = i.split(';') #split the string at the semi-colon delimiter
    game_subtotal = 0 #subtotal for each draw within a round
    for game in subset:
        total_blue = 0
        total_red = 0
        total_green = 0

      

        #Regex expressions to find the number before each color
        result_blue = re.findall(r'(\d+) blue', game)
        result_red = re.findall(r'(\d+) red', game)
        result_green = re.findall(r'(\d+) green', game)

        #Handle empty cases
        if len(result_green) == 0:
            result_green = ['0']
        if len(result_red) == 0:
            result_red = ['0']
        if len(result_blue) == 0:
            result_blue = ['0']
        
       
       #convert each result to int & check if total number of color is above the minimum required for the game
        total_red = int(result_red[0])
        if total_red > min_red:
            min_red = total_red
        total_blue = int(result_blue[0])
        if total_blue > min_blue:
            min_blue = total_blue
        total_green = int(result_green[0])
        if total_green > min_green:
            min_green = total_green
        
        

        #check if any draw from the bag contains a color outside the limits of the game
        if(total_blue>max_blue or total_green>max_green or total_red>max_red):
            game_subtotal += 1
        print('subscore' + str(game_subtotal))
    
    #Calculate power per the game rules & add to the overall power score for each round
    power_total = min_green * min_blue * min_red
    power += power_total
    print(power)
    
    #If no games contained draws outside the limits, add the round number to the overall score
    if game_subtotal == 0:
        score += round
    

print("final score is " + str(score))
