with open('day9/data.txt', 'r') as file:
    # read the entire file and store each character in a list
    line = file.readline().strip()
    # convert the string into a list of integers
    digits = [int(char) for char in line]

numOfFiles = []
freeSpace = []
for index, digit in enumerate(digits):
    if index % 2 == 0:
        numOfFiles.append(digit)
    else:
        freeSpace.append(digit)
#print(digits)
#print(numOfFiles)
#print(freeSpace)

#logic to convert disk
newDisk = []
numberDisk = []
for i in range(len(numOfFiles)):
    id = i
    for count in range(numOfFiles[i]):
        newDisk.append(id)
        numberDisk.append(id)
    if i < len(numOfFiles)-1:
        for count in range(freeSpace[i]):
            newDisk.append(".")

#print(newDisk)

indices_to_swap = []
charCount = 0

for index, char in enumerate(newDisk):
    if (char == "."):
        charCount += 1
        indices_to_swap.append(index)
        
#print(indices_to_swap)

k=len(numberDisk)-1
j = len(newDisk)-1
removeCount = 0

#print(numberDisk)
for index in indices_to_swap:
    if index < j:
        newDisk[index] = numberDisk[k]
        k -= 1
        removeCount += 1
    else:
        break
    j -= 1
#print(removeCount)

MyCount = 0
IndexCount = 0
reverseDisk = newDisk[::-1]
#print(reverseDisk)
while MyCount < removeCount:
    if reverseDisk[IndexCount] != ".":
        reverseDisk[IndexCount] = "."
        MyCount += 1
        #print(MyCount)
        #print(reverseDisk)
    IndexCount += 1

#print(reverseDisk)
newDisk = reverseDisk[::-1]

#JustForShow = newDisk.copy()
#while charCount != 0:
  #  JustForShow.append(".")
    #charCount -= 1

mySum = 0

for i in range(len(newDisk)-1):
    if newDisk[i] != ".":
        mySum += newDisk[i]*i
        #print(mySum)

#print(JustForShow)
#print(newDisk)
print(mySum)
#print(numberDisk)