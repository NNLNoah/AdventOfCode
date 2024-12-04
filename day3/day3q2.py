import re

sum=0
mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

with open("day3/data.txt", 'r') as file:
    memory = file.read()
    enabled = True

    for match in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory):
        text = match.group(0) # returns as string
        if do_pattern.fullmatch(text): # checks if regex of do matches text
            enabled = True
        elif dont_pattern.fullmatch(text): # checks if regex od dont matches text
            enabled = False
        else:
            if enabled: 
                x, y = map(int, mul_pattern.match(text).groups()) #checks if regex matches text, groups the two numbers as strings in a tuple, and converts them to integers
                sum += x * y
print(sum)