#things to keep in mind: all antinodes are added even overlapped
#                        if antinode is off the map, doesnt count
#                        
# find all instances of a frequency, find all possible pairs, find i and j distance (pattern), find antinodes according to pattern, confirm antinode is on the map, add to sum
import re

with (open ('day8/data.txt', 'r')) as file:
    #read lines without the \n at the end
    lines = [line.strip() for line in file.readlines()]

typeOfFrequencies = []
antinodes = []

for line in lines:
    # if character is not a dot, add to list of typeOfFrequencies
    for character in line:
        if character != '.':
            if character not in typeOfFrequencies:
                typeOfFrequencies.append(character)
#print(typeOfFrequencies)


for frequency in typeOfFrequencies:
    # find all instances of a frequency
    instances = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == frequency:
                instances.append((i,j))
    
    # find all possible pairs
    pairs = []
    for i in range(len(instances)-1):
        for j in range(i+1, len(instances)):
            pairs.append((instances[i], instances[j]))
    
    for pair in pairs:
        # find i and j distance (pattern)
        iDist = pair[1][0] - pair[0][0]
        jDist = pair[1][1] - pair[0][1]
        
        # find antinodes according to pattern
        
        antinode1 = (pair[0][0] - iDist, pair[0][1] - jDist)
        antinode2 = (pair[1][0] + iDist, pair[1][1] + jDist)

        if antinode1[0] >= 0 and antinode1[0] < len(lines) and antinode1[1] >= 0 and antinode1[1] < len(lines[0]):
            if(antinode1 not in antinodes):
                antinodes.append(antinode1)
        if antinode2[0] >= 0 and antinode2[0] < len(lines) and antinode2[1] >= 0 and antinode2[1] < len(lines[0]):
            if(antinode2 not in antinodes):
                antinodes.append(antinode2)
#print(antinodes)

print(antinodes.__len__())