import re

# Open and read the file
with open('Day 4/input.txt', 'r') as file:
    content = file.read()

# Convert the content into a grid of letters
lines = [list(line.strip()) for line in content.split('\n') if line.strip()]

def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    found_positions = []

    def search(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    found_positions.append((i, j, dx, dy))

    return found_positions

# Find all instances of "XMAS" in the grid
positions = find_word(lines, "XMAS")

# Print the total count of instances of "XMAS"
print("Part 1:", len(positions))