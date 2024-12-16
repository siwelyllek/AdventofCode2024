# Open and read the file
with open('Day 6/input.txt', 'r') as file:
    content = file.read()

# Convert the content into a grid of characters
grid = [list(line) for line in content.split('\n') if line.strip()]

# Define the directions and their corresponding movements
directions = {
    '^': (-1, 0),  # Up
    '>': (0, 1),   # Right
    'v': (1, 0),   # Down
    '<': (0, -1)   # Left
}

# Define the order of directions for turning right
turn_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

# Find the guard's starting position and direction
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell in directions:
            guard_pos = (i, j)
            guard_dir = cell
            break

# Track the positions visited by the guard
visited_positions = set()
visited_positions.add(guard_pos)

# Simulate the guard's movement
while True:
    x, y = guard_pos
    dx, dy = directions[guard_dir]
    nx, ny = x + dx, y + dy

    # Check if the guard is about to leave the grid
    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
        break

    # Check if there is an obstacle in front of the guard
    if grid[nx][ny] == '#':
        guard_dir = turn_right[guard_dir]
    else:
        guard_pos = (nx, ny)
        visited_positions.add(guard_pos)

# Print the number of distinct positions visited by the guard
print("Part 1:", len(visited_positions))

