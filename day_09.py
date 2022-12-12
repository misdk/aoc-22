from dataclasses import dataclass


@dataclass
class Operation:
    direction: str
    value: int

    @staticmethod
    def from_string(string):
        tokens = string.split()
        return Operation(tokens[0], int(tokens[1]))


def read_input(file_name) -> list[Operation]:
    with open(file_name) as file:
        lines = [line.strip() for line in file.readlines()]
        return list(map(Operation.from_string, lines))


class Grid:
    def __init__(self, rope_size, start=(0, 0)):
        self._points = [start for _ in range(rope_size)]
        self._tail_history = set()
        self._tail_history.add(self._points[-1])

    def move(self, direction):
        self._move_head(direction)

        for index in range(1, len(self._points)):
            self._move_point(index)

        self._tail_history.add(self._points[-1])

    def _move_head(self, direction):
        move_x, move_y = Grid._direction_to_vector(direction)
        head_x, head_y = self._points[0]
        self._points[0] = head_x + move_x, head_y + move_y

    def _move_point(self, point_index):
        tail = self._points[point_index]
        head = self._points[point_index - 1]

        tail_to_head = head[0] - tail[0], head[1] - tail[1]
        x, y = tail_to_head

        if abs(x) <= 1 and abs(y) <= 1:
            return

        move_x = 0 if x == 0 else x / abs(x)
        move_y = 0 if y == 0 else y / abs(y)

        self._points[point_index] = tail[0] + move_x, tail[1] + move_y

    def get_tail_positions(self):
        return len(self._tail_history)

    @staticmethod
    def _direction_to_vector(direction):
        if direction == 'L':
            return (-1, 0)
        if direction == 'U':
            return (0, 1)
        if direction == 'R':
            return (1, 0)
        if direction == 'D':
            return (0, -1)
        exit(-1, 'Unhandled direction')


def solve(operations, rope_size):
    grid = Grid(rope_size=rope_size)
    for operation in operations:
        for _ in range(operation.value):
            grid.move(operation.direction)
    return grid.get_tail_positions()


def part_1(operations):
    print(solve(operations, 2))


def part_2(operations):
    print(solve(operations, 10))


def main():
    operations = read_input('day_9_input.txt')
    part_1(operations)
    part_2(operations)


if __name__ == '__main__':
    main()
