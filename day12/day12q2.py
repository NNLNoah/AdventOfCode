with open('day12/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

gardens = []


def lookLeft(i, j, path, currChar, visited):
    if j - 1 >= 0 and lines[i][j - 1] == currChar and (i, j-1) not in visited:
        visited.add((i, j-1))
        group.append((i, j-1))

        recursivePath(i, j-1, group, currChar, visited)

def lookRight(i, j, path, currChar, visited):
    if j + 1 < len(lines[0]) and lines[i][j + 1] == currChar and (i, j+1) not in visited:
        visited.add((i, j+1))
        group.append((i, j+1))
        recursivePath(i, j+1, group, currChar, visited)

def lookUp(i, j, path, currChar, visited):
    if i - 1 >= 0 and lines[i - 1][j] == currChar and (i-1, j) not in visited:
        visited.add((i-1, j))
        group.append((i-1, j))
        recursivePath(i-1, j, group, currChar, visited)

def lookDown(i, j, path, currChar, visited):
    if i + 1 < len(lines) and lines[i + 1][j] == currChar and (i+1, j) not in visited:
        visited.add((i+1, j))
        group.append((i+1, j))
        recursivePath(i+1, j, group, currChar, visited)

def recursivePath(i, j, path, currChar, visited):
    lookLeft(i, j, path, currChar, visited)
    lookRight(i, j, path, currChar, visited)
    lookUp(i, j, path, currChar, visited)
    lookDown(i, j, path, currChar, visited)
    
visited = set()

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i, j) not in visited:
            point = (i, j)
            currChar = lines[i][j]
            #print(point)
            #print(currChar)
            group = [point]
            visited.add(point)
            recursivePath(i, j, group, currChar, visited)
            gardens.append(group)

totalPrice = 0
for garden in gardens:
    print(garden)
    area = len(garden)
    totalGardenPerimeter = 0
    for k in range(len(garden)):
        numOfSidesTouching = 0
        i, j = garden[k]
        for l in range(len(garden)):
            if k != l:
                m, n = garden[l]
                if abs(i - m) + abs(j - n) == 1:
                    numOfSidesTouching += 1
        charPerimeter = 4 - numOfSidesTouching
        totalGardenPerimeter += charPerimeter
    print(totalGardenPerimeter)
    price = area * totalGardenPerimeter
    totalPrice += price
print(totalPrice)

