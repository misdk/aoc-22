def read_input(file_name):
    with open(file_name) as file:
        lines = [line.strip() for line in file.readlines()]
        lines = [line for line in lines]
    return lines


def part_1(grid):
    visible_trees = set()

    # left
    for x in range(len(grid)):
        max_height = None
        for y in range(len(grid[x])):
            if max_height == None or grid[x][y] > max_height:
                max_height = grid[x][y]
                visible_trees.add((x, y))
    
    # top
    for y in range(0, len(grid[0])):
        max_height = None
        for x in range(0, len(grid)):
            if max_height == None or grid[x][y] > max_height:
                max_height = grid[x][y]
                visible_trees.add((x, y))
    
    # right
    for x in range(len(grid)):
        max_height = None
        for y in range(len(grid[x]) - 1, -1, -1):
            if max_height == None or grid[x][y] > max_height:
                max_height = grid[x][y]
                visible_trees.add((x, y))
    
    # bottom
    for y in range(0, len(grid[0])):
        max_height = None
        for x in range(len(grid) - 1, -1, -1):
            if max_height == None or grid[x][y] > max_height:
                max_height = grid[x][y]
                visible_trees.add((x, y))

    print(len(visible_trees))


def move(point, direction, grid_size):
    x, y = point
    size_x, size_y = grid_size
    if direction == 'top':
        return (x, y + 1) if y + 1 < size_y else None
    if direction == 'bottom':
        return (x, y - 1) if y - 1 >= 0 else None
    if direction == 'left':
        return (x - 1, y) if x - 1 >= 0 else None
    if direction == 'right':
        return (x + 1, y) if x + 1 < size_x else None
    exit(-1, 'move error')


def part_2(grid):
    answer = 0
    grid_size = len(grid), len(grid[0])
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            trees_numbers = []
            for direction in ['top', 'bottom', 'left', 'right']:
                current_point = x, y
                visible_trees_number = 0
                current_point = move(current_point, direction, grid_size)
                
                while current_point != None:
                    current_x, current_y = current_point
                    if grid[x][y] > grid[current_x][current_y]:
                        visible_trees_number += 1
                    elif grid[x][y] == grid[current_x][current_y]: 
                        visible_trees_number += 1
                        break
                    else:
                        break
                    current_point = move(current_point, direction, grid_size)
            
                trees_numbers.append(visible_trees_number)
            
            candidate = trees_numbers[0] * trees_numbers[1] * trees_numbers[2] * trees_numbers[3]
            if candidate > answer:
                answer = candidate

    print(answer)


def main():
    grid = read_input('day_8_input.txt')
    part_1(grid)
    part_2(grid)


if __name__ == '__main__':
    main()
