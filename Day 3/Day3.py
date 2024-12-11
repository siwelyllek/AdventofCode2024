import re

# Open and read the file
with open('Day 3/input.txt', 'r') as file:
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
matches_part2 = []
enabled = True

for line in lines:
    parts = re.split(r'(do\(\)|don\'t\(\))', line)
    for part in parts:
        if part == "do()":
            enabled = True
        elif part == "don't()":
            enabled = False
        elif enabled:
            for match in pattern.finditer(part):
                start_index = match.start()
                x, y = match.groups()
                matches_part2.append(( int(x), int(y) ))

# Multiply the numbers in each match and sum the total for part 2
total_sum_part2 = sum(x * y for x, y in matches_part2)

print("Part 2:", total_sum_part2)


