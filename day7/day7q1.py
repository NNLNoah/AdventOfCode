import re

with (open ('day7/data.txt', 'r')) as file:
    lines = file.readlines()

sum = 0
# regex to separate each number in this line into variables 190: 10 19
for line in lines:
    matches = list(map(int, re.findall(r'\d+', line)))
    answer = matches[0]
    matches.pop(0)

    #check if matches can add or multiply to answer
    def recursiveCheck(matches, answer):
        for i in range(len(matches)-1):
            addResult = matches[i] + matches[i+1]
            multResult = matches[i] * matches[i+1]
            if len(matches) == 2:
                if addResult == answer:
                    print("true", addResult)
                    return True
                if multResult == answer:
                    print("true", multResult)
                    return True
                else:
                    return False
            else:
                if recursiveCheck([addResult] + matches[i+2:], answer):
                    return True
                if recursiveCheck([multResult] + matches[i+2:], answer):
                    return True

    if recursiveCheck(matches, answer):
        sum += answer

print(sum)