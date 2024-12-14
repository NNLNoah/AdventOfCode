with(open ('day6/data.txt', 'r')) as file:
    lines = file.readlines()
    currChar = '^'

    #function goingDown():
       # currChar = 'v'
        
    # find starting point
    startingPoint = None
    for i in range(len(lines)-1):
        for j in range(len(lines[0])):
            if lines[i][j] == currChar:
                startingPoint = (i, j)
                break
    #replace startingPoint char with a dot
    lines[startingPoint[0]] = lines[startingPoint[0]][:startingPoint[1]] + '.' + lines[startingPoint[0]][startingPoint[1]+1:]
    # find the path
    path = []
    distinct_locations = []
    distinct_locations.append(startingPoint)
    path.append(startingPoint)
    i, j = startingPoint
    sum = 1

    while True:
        if currChar == '^':
            if i > 0 and lines[i-1][j] == '.':
                i -= 1
            elif i > 0 and lines[i-1][j] == '#':
                j += 1
                currChar = '>'
            else:
                break
        elif currChar == '>':
            if j < len(lines[0])-1 and lines[i][j+1] == '.':
                j += 1
            elif j < len(lines[0])-1 and lines[i][j+1] == '#':
                i += 1
                currChar = 'v'
            else:
                break
        elif currChar == 'v':
            if i < len(lines)-1 and lines[i+1][j] == '.':
                i += 1
            elif i < len(lines)-1 and lines[i+1][j] == '#':
                j -= 1
                currChar = '<'
            else:
                break
        elif currChar == '<':
            if j > 0 and lines[i][j-1] == '.':
                j -= 1
            elif j > 0 and lines[i][j-1] == '#':
                i -= 1
                currChar = '^'
            else:
                break
        path.append((i, j))
        #if the touple dne in the path, increase sum
        if (i,j) not in distinct_locations:
            distinct_locations.append((i,j))
            sum += 1
    print(sum)