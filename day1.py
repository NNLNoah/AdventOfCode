# parse file
files = "data.txt"

#sort list
list1 = []
list2 = []

with open(files, 'r') as file:
    for line in file:
        a, b = line.split()  # Split by whitespace
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

sum=0

for i in range(len(list1)):
    diff = abs(list2[i] - list1[i])
    sum += diff

print(sum)