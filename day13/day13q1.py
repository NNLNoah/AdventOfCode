import re

with (open('day13/data.txt')) as file:
    data = file.read()

button_pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
results = []

# Find all matches in the data
matches = re.findall(button_pattern, data)
print(matches)
for match in matches: 
    button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = map(int, match) # Convert all the values to integers 