import re

# Open and read the file
with open('Day 2/input.txt', 'r') as file:
    content = file.read()

# Use regex to find all lines
lines = re.findall(r'.+', content)

# Store each line into its own list
line_lists = [list(map(int, line.split())) for line in lines]

def is_increasing_or_decreasing(lst):
    increasing = all(x < y for x, y in zip(lst, lst[1:]))
    decreasing = all(x > y for x, y in zip(lst, lst[1:]))
    return increasing or decreasing

def has_valid_differences(lst):
    return all(1 <= abs(x - y) <= 3 for x, y in zip(lst, lst[1:]))

def is_valid_list(lst):
    if is_increasing_or_decreasing(lst) and has_valid_differences(lst):
        return True
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if is_increasing_or_decreasing(new_lst) and has_valid_differences(new_lst):
            return True
    return False

valid_lists_part1 = []
for lst in line_lists:
    if is_increasing_or_decreasing(lst) and has_valid_differences(lst):
        valid_lists_part1.append(lst)

print("Part 1:", len(valid_lists_part1))

# Part 2
valid_lists_part2 = []
for lst in line_lists:
    if is_valid_list(lst):
        valid_lists_part2.append(lst)

print("Part 2:", len(valid_lists_part2))