with open('input.txt', 'r') as file:
    #Read the file line by line
    lines = file.readlines()

input = []
score = 0

for line in lines:
    input.append(line.strip())


#input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'] #Test Input
for i in input:
    value = ''
    for letter in i:
        if letter.isnumeric() == True:
            value += letter
    size = len(value)
    if size == 1:
        value += value[0]    
    elif size >2:
        value = value[0] + value[size-1]
    print(value)
    score += int(value)
print("final score is " + str(score))
