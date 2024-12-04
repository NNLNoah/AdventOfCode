# Description: Write a program to read a file, if string mul(num, num)is found in file using regex, multiply the two numbers and add the result to a sum variable.
# The file contains lines of random keysThe program should read the file and calculate the sum of the differences between the two lists.
files = "day3/data.txt"

#if string mul(num, num) is found in file using regex, multiply the two numbers and add the result to a sum variable    
import re
sum = 0
with open(files, 'r') as file:
    for line in file:
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        for match in matches:
            a, b = re.findall(r'\d+', match)
            sum += int(a) * int(b)

print(sum)