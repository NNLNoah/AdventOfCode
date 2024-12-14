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
    loops = []
    path.append(startingPoint)
    i, j = startingPoint
    sum = 1
    obstacles = []
    sumOfObstacles = 0

    while True:
        if currChar == '^':
            if len(loops) > 3 and i == loops[-3][0]:
                obstacles.append((i-1,j))
                sumOfObstacles += 1
            if i > 0 and lines[i-1][j] == '.':
                i -= 1
            elif i > 0 and lines[i-1][j] == '#':
                loops.append((i,j))
                j += 1
                currChar = '>'
                

            else:
                break
        elif currChar == '>':
            if len(loops) > 3 and j == loops[-3][1]:
                obstacles.append((i,j+1))
                sumOfObstacles += 1
            if j < len(lines[0])-1 and lines[i][j+1] == '.':
                j += 1
            elif j < len(lines[0])-1 and lines[i][j+1] == '#':
                loops.append((i,j))
                i += 1
                currChar = 'v'
                
            else:
                break
        elif currChar == 'v':
            if len(loops) > 3 and i == loops[-3][0]:
                obstacles.append((i+1,j))
                sumOfObstacles += 1
            if i < len(lines)-1 and lines[i+1][j] == '.':
                i += 1
            elif i < len(lines)-1 and lines[i+1][j] == '#':
                loops.append((i,j))
                j -= 1
                currChar = '<'
                
            else:
                break
        elif currChar == '<':
            if len(loops) > 3 and j == loops[-3][1]:
                obstacles.append((i,j-1))
                sumOfObstacles += 1
            if j > 0 and lines[i][j-1] == '.':
                j -= 1
            elif j > 0 and lines[i][j-1] == '#':
                i -= 1
                currChar = '^'
            else:
                break
        path.append((i, j))

    print(obstacles)
    print(sumOfObstacles)

# (1,4) (1,8)
# (4,4) (4,8)