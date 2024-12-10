import re
from collections import Counter

# Open and read the file
with open('Day 1/input.txt', 'r') as file:
    content = file.read()

# Use regex to find all pairs of numbers
matches = re.findall(r'(\d+)\s+(\d+)', content)

# Separate the numbers into two lists
list1 = [int(match[0]) for match in matches]
list2 = [int(match[1]) for match in matches]

# Sort the lists
list1.sort()
list2.sort()

# Find the differences and store in a new list
differences = [abs(a - b) for a, b in zip(list1, list2)]

# Sum the differences
total_difference = sum(differences)

# print("List 1:", list1)
# print("List 2:", list2)
# print("Differences:", differences)
print("Part 1:", total_difference)

# Part 2
# Count occurrences of each number in list2
counter_list = Counter(list2)

# Create a list of tuples with each number in list1 and its count in list2
count_list = [(num, counter_list[num]) for num in list1]

# Multiply each tuple and sum the results
total_product_sum = sum(num * count for num, count in count_list)

# print("Count List:", count_list)
print("Part 2:", total_product_sum)