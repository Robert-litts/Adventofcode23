with open('input_aoc3.txt', 'r') as file:
    #Read the file line by line
    lines = file.readlines()

input = []

for line in lines:
    input.append(line.strip())

#Test Input
'''
input = [
'467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']
'''

numbers = set() #set to store coordinates of numbers found

r = -1
for row in input:
    r+=1
    c = -1
    for char in row:
        c+=1
        
        if char.isnumeric() == False and char != '.': #only look for symbols (i.e. no numbers and no periods)
            print(char)
        
            for rr in [r-1, r, r+1]: #search rows /columns in the six positions around any single symbol
                #print(rr)
                for cc in [c-1, c, c+1]:
                    if rr <0 or rr > len(row) or cc < 0 or cc > int(len(input[0]))-1: #check to make sure not out of bounds
                       continue

                    
                    
                    if (input[rr][cc]).isnumeric(): #if there is a number in any adjacent position
                        num=0
                        while (input[rr][cc+num-1]).isnumeric(): #find the start of the number
                            num -=1
                        numbers.add((rr, cc+num)) #add the coordinates to the set of numbers
                           

score = 0

#search the set of coordinates (x,y) in the set 'numbers' to find all part numbers
for x, y in numbers:
    num = 0
    #find how many digits the number is
    while y+num+1 < int(len(input[0])) and input[x][y+num+1].isnumeric():
        num +=1
    #based on the number of digits, add the part number to the score
    score += int(input[x][y:y+num+1])              

print(score)
