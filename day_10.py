def read_input(file_name):
    with open(file_name) as file:
        return [line.strip().split() for line in file.readlines()]


def commands_to_values(commands):
    result = []
    for command in commands:
        if command[0] == 'noop':
            result.append(0)
        if command[0] == 'addx':
            result.extend([0, int(command[1])])
    return result


def part_1(commands):
    special_cycles = [20, 60, 100, 140, 180, 220]
    values = commands_to_values(commands)
    answer = 0
    x = 1

    for index, value in enumerate(values):
        cycle_number = index + 1
        if any([cycle_number == x for x in special_cycles]):
            answer += cycle_number * x
        x += value

    print(answer)


def part_2(commands):
    values = commands_to_values(commands)
    crt_memory = []
    x = 1

    for crt_position, value in enumerate(values):
        crt_memory.append('#' if abs(crt_position % 40 - x) <= 1 else '.')
        x += value

    matrix = [crt_memory[i*40:(i+1)*40] for i in range(len(crt_memory) // 40)]
    for row in matrix:
        print("".join(row))


def main():
    commands = read_input('day_10_input.txt')
    part_1(commands)
    part_2(commands)


if __name__ == '__main__':
    main()
