from collections import namedtuple


Operation = namedtuple('Operation', 'number start end')


def parse_stacks_state(file):
    lines = []
    line = file.readline()
    while line != '\n':
        lines.append(line)
        line = file.readline()
    lines = lines[::-1]
    
    state = []
    for index, firs_ch in enumerate(lines[0]):
        if firs_ch < '0' or firs_ch > '9':
            continue
        state.append([])
        for i in range(1, len(lines)):
            ch = lines[i][index]
            if ch != ' ':
                state[len(state) - 1].append(ch)
    return state


def parse_operations(file):
    lines = [line.strip().split() for line in file]
    return [Operation(int(line[1]), int(line[3]) - 1, int(line[5]) - 1) for line in lines]


def parse_input_from_file(file_name):
    with open(file_name) as file:
        return parse_stacks_state(file), parse_operations(file)


def get_answer(state):
    answer = ''
    for stack in state:
        answer += stack[len(stack) - 1]
    return answer


def part1():
    state, operations = parse_input_from_file('day_5_part_1_input.txt')

    for op in operations:
        for _ in range(op.number):
            block = state[op.start].pop()
            state[op.end].append(block)
    
    print(get_answer(state))


def part2():
    state, operations = parse_input_from_file('day_5_part_2_input.txt')

    for op in operations:
        stack = state[op.start]
        state[op.start] = stack[:-op.number]
        state[op.end].extend(stack[-op.number:])

    print(get_answer(state))


if __name__ == '__main__':
    part1()
    part2()
