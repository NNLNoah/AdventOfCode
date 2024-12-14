with open('day5/data.txt', 'r') as file:
    lines = file.readlines()

pairs = [tuple(map(int, line.strip().split('|'))) for line in lines]

tree = {}

for parent, child in pairs:
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

all_children = {child for children in tree.values() for child in children}
roots = {parent for parent in tree if parent not in all_children}

# now read list of numbers and check if they are a branch in the tree
print(roots)
with open('day5/data2.txt', 'r') as file:
    lines = file.readlines()

goodOperations = []

for line in lines:
    numlist = [int(num) for num in line.split(',')]
    good = True
    for i in range(len(numlist)-1):
        parent = numlist[i]
        child = numlist[i+1]
        if child not in tree.get(parent, []):
            good = False
            break
    if good:
        goodOperations.append(numlist)
    
print(goodOperations)
sum = 0

for operation in goodOperations:
    middle = operation[(len(operation)-1)//2]
    sum += middle
    print(middle)
print(sum)