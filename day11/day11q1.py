with ( open ( 'day11/data.txt' ) ) as file:
    line = file.readline().split()
    stones = [int(x) for x in line]
    # how to store all numbers in the line in a list seperated by a space
    currStones = [x for x in line]
#print(stones)
       
newStones = []
count = 0

def checkStones(stonesString):
    for stone in stonesString:
        if stone == '0':
            newStones.append('1')
        elif len(stone) % 2 == 0:
            left = stone[:len(stone)//2]
            right = stone[len(stone)//2:]
            # check if right is just a string of 0s
            if right == '0'*len(right):
                right = '0'
            #elif right has 0s at the start
            elif right[0] == '0':
                while right[0] == '0':
                    right = right[1:]
            newStones.append(left)
            newStones.append(right)
        else: 
            stone2024 = str(int(stone) * 2024)
            newStones.append(stone2024)

while count < 25:
    checkStones(currStones)
    currStones = newStones
    #print(currStones)
    newStones = []
    count += 1

print(len(currStones))