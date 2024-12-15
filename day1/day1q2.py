# parse file
files = "data.txt"

leftList = []
rightList = []

with open(files, 'r') as file:
    for line in file:
        a, b = line.split()  # Split by whitespace
        leftList.append(int(a))
        rightList.append(int(b))

sum=0
my_map = {}

for num in leftList:
    my_map[num] = 0

for num in rightList:
    if num in my_map:
       my_map[num] += 1

for num in my_map:
    sum += num * my_map[num]

print(sum)