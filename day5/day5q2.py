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
badOperations = []
for line in lines:
    numlist = [int(num) for num in line.split(',')]
    good = True
    for i in range(len(numlist)-1):
        parent = numlist[i]
        child = numlist[i+1]
        if child not in tree.get(parent, []): # if child is not in the list of children of the parent
            good = False
            badOperations.append(numlist)
            break
    if good:
        goodOperations.append(numlist)

print(badOperations)
total_sum = 0
# Fix bad operations
for operation in badOperations:
    fixed = []
    for num in operation:
        if not fixed or num in tree.get(fixed[-1], []):
            fixed.append(num)
        else:
            # Find a valid position for num
            for i in range(len(fixed)):
                if num in tree.get(fixed[i], []):
                    fixed.insert(i + 1, num)
                    break
    operation[:] = fixed

print("Bad operations (after fix):", badOperations)

for badOp in badOperations:
    middle = badOp[(len(badOp)-1)//2]
    total_sum += middle
    print(middle)
print(total_sum)