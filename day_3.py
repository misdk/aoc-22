def get_items(string: str):
    half_size = len(string) // 2
    first_half = string[:half_size]
    second_half = string[half_size:]

    chars = set()
    for ch in first_half:
        chars.add(ch)

    result = set()
    for ch in second_half:
        if ch in chars and ch not in result:
            result.add(ch)

    return result


def item_value(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    if item >= 'A' and item <= 'Z':
        return ord(item) - ord('A') + 27
    exit(-1)


def part1():
    with open('day_3_part_1_input.txt') as file:
        answer = 0
        for line in file:
            string = line.strip()
            items = get_items(string)
            for item in items:
                answer += item_value(item)
    print(answer)


def create_groups(lines):
    groups = []
    num = 0
    for line in lines:
        if num == 0:
            groups.append([])
        groups[len(groups) - 1].append(line)
        num = (num + 1) % 3
    return groups


def get_items_for_group(group):
    first = group[0]
    second = group[1]
    third = group[2]

    first_set = set()
    second_set = set()
    third_set = set()
    for ch in first:
        first_set.add(ch)
    for ch in second:
        second_set.add(ch)
    for ch in third:
        third_set.add(ch)
    
    return first_set.intersection(second_set).intersection(third_set)


def part2():
    with open('day_3_part_2_input.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    groups = create_groups(lines)
    answer = 0
    for group in groups:
        items = get_items_for_group(group)
        for item in items:
            answer += item_value(item)
    print(answer)


if __name__ == '__main__':
    part1()
    part2()