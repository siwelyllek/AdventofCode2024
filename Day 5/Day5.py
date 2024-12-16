import re

# Open and read the file
with open('Day 5/input.txt', 'r') as file:
    content = file.read()

# Split the content into two parts using the blank line as the delimiter
parts = content.split('\n\n')

# Process the first part to extract lines with two integers split by a |
group1 = [line for line in parts[0].split('\n') if '|' in line]

# Process the second part to extract lines with comma-separated numbers
group2 = [line for line in parts[1].split('\n') if ',' in line]

# Parse the rules in group1
rules = [(int(a), int(b)) for line in group1 for a, b in [line.split('|')]]

def follows_rules(pages, rules):
    page_indices = {page: i for i, page in enumerate(pages)}
    for a, b in rules:
        if a in page_indices and b in page_indices and page_indices[a] > page_indices[b]:
            return False
    return True

# Check each line in group2 to see if it follows the rules
valid_lines = []
invalid_lines = []
for line in group2:
    pages = list(map(int, line.split(',')))
    if follows_rules(pages, rules):
        valid_lines.append(pages)
    else:
        invalid_lines.append(pages)

# Extract the middle values from each valid line and sum them
middle_values_sum = 0
for pages in valid_lines:
    if len(pages) > 0:
        middle_index = len(pages) // 2
        middle_values_sum += pages[middle_index]

print("Sum of middle values:", middle_values_sum)

# Order the pages in invalid lines correctly according to the rules
def order_pages(pages, rules):
    ordered_pages = pages[:]
    changed = True
    while changed:
        changed = False
        for a, b in rules:
            if a in ordered_pages and b in ordered_pages:
                a_index = ordered_pages.index(a)
                b_index = ordered_pages.index(b)
                if a_index > b_index:
                    ordered_pages.remove(a)
                    ordered_pages.insert(b_index, a)
                    changed = True
    return ordered_pages
ordered_invalid_lines = [order_pages(pages, rules) for pages in invalid_lines]

# Extract the middle values from each valid line and sum them
middle_values_sum2 = 0
for pages in ordered_invalid_lines:
    if len(pages) > 0:
        middle_index = len(pages) // 2
        middle_values_sum2 += pages[middle_index]

print("Sum Invalid Lines:", middle_values_sum2)