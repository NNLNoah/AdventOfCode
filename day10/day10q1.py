with open('day10/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

trailheads = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '0':
            point = (i, j)
            trailheads.append(point)

print(trailheads)
paths = []

def lookLeft(i, j, count, path):
    if j - 1 >= 0 and int(lines[i][j - 1]) == count:
        new_path = path.copy()
        new_path.append((i, j-1))
        recursivePath(i, j-1, count, new_path)

def lookRight(i, j, count, path):
    if j + 1 < len(lines[0]) and int(lines[i][j + 1]) == count:
        new_path = path.copy()
        new_path.append((i, j+1))
        recursivePath(i, j+1, count, new_path)

def lookUp(i, j, count, path):
    if i - 1 >= 0 and int(lines[i - 1][j]) == count:
        new_path = path.copy()
        new_path.append((i-1, j))
        recursivePath(i-1, j, count, new_path)

def lookDown(i, j, count, path):
    if i + 1 < len(lines) and int(lines[i + 1][j]) == count:
        new_path = path.copy()
        new_path.append((i+1, j))
        recursivePath(i+1, j, count, new_path)

def recursivePath(i, j, count, path):
    if count == 9:
        paths.append(path)
    elif 0 <= i < len(lines) and 0 <= j < len(lines[0]):
        count += 1
        lookLeft(i, j, count, path)
        lookRight(i, j, count, path)
        lookUp(i, j, count, path)
        lookDown(i, j, count, path)

for trailhead in trailheads:
    i, j = trailhead
    count = 0
    path = [trailhead]
    recursivePath(i, j, count, path)

pathTypes = []

path_dict = {}


for path in paths:
    start_point = path[0]
    end_point = path[-1]
    if start_point not in path_dict:
        path_dict[start_point] = []
    # Check if the end point is unique for the given start point
    if all(end_point != existing_path[-1] for existing_path in path_dict[start_point]):
        path_dict[start_point].append(path)

pathTypes = list(path_dict.values())
print(pathTypes)
sum = 0
for pathType in pathTypes:
    for path in pathType:
        sum += 1
print(sum)