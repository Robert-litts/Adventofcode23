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
adjacent = 0
count = set()
part2 = set()
part2_score = set()
final_score = 0
checklist = []
anotherset = set()
r = -1
for row in input:
    r+=1
    c = -1
    
    for char in row:
        c+=1
        
        if char == '*': #only look for * symbols
            adjacent += 1
            #print(adjacent)

            
            for rr in [r-1, r, r+1]: #search rows /columns in the six positions around any single symbol
                #print(rr)
                for cc in [c-1, c, c+1]:
                    if rr <0 or rr > len(row) or cc < 0 or cc > int(len(input[0]))-1: #check to make sure not out of bounds
                       continue

                    if (input[rr][cc]).isnumeric(): #if there is a number in any adjacent position
                        
                        num=0
                        while (input[rr][cc+num-1]).isnumeric(): #find the start of the number
                            num -=1
                        numbers.add((rr, cc+num, adjacent)) #add the coordinates to the set of numbers
                           

#code below counts how many times an adjacent number appears for each gear
for i in range (1,adjacent+1):
    counter = 0
    for x, y, z in numbers:
        if i == z:
            counter +=1
    count.add((i, counter))

#creates a separate list for only gears that have exactly 2 adjacent numbers
for x, y in count:
    if y == 2:
        for p, q, r in numbers:
            if x == r:
                part2.add((p, q, r))



score = 0

#search the set of coordinates (x,y) in the set 'numbers' to find all part numbers
for x, y, z in part2:
    num = 0
    #find how many digits the number is
    while y+num+1 < int(len(input[0])) and input[x][y+num+1].isnumeric():
        num +=1
    #based on the number of digits, add the part number to the score
    score = int(input[x][y:y+num+1])              
    part2_score.add((score,z)) #add an identifier for the gear number to the coordinate list

#iterate over the list of scores and gear numbers
for x, y in part2_score:

    for r, s in part2_score:     
        if (x == r and y == s): #check against itself
            continue
        elif y == s and checklist.count(y)==0: #check if the gear number matches and was not already compared
            checklist.append(y)
            final_score+= (r * x)
            
print(final_score)
