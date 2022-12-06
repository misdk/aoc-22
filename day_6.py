def parse_input(file_name):
    with open(file_name) as file:
        return file.readline().strip()


def check_is_unique(values): 
    values_set = set()
    for value in values:
        values_set.add(value)
    return len(values) == len(values_set)


def find_marker_index(message, number):
    for i in range(len(message) - number):
        buffer = message[i:i + number]
        if check_is_unique(buffer):
            return i + number
    exit(-1)


def part1():
    message = parse_input('day_6_part_1_input.txt')
    answer = find_marker_index(message, 4)
    print(answer)


def part2():
    message = parse_input('day_6_part_2_input.txt')
    answer = find_marker_index(message, 14)
    print(answer)


if __name__ == '__main__':
    part1()
    part2()
