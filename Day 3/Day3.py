import re

# Open and read the file
with open('Day 3/test2.txt', 'r') as file:
    content = file.read()

# Use regex to find all lines
lines = re.findall(r'.+', content)

# Find the exact match of mul(X,Y) where X and Y are integers in each line
pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
matches = [pattern.findall(line) for line in lines]




# Flatten the list of matches
matches = [match for sublist in matches for match in sublist]

# Multiply the numbers in each match and sum the total
total_sum = sum(int(x) * int(y) for x, y in matches)

print("Part 1:", total_sum)

# Part 2
