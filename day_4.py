from collections import namedtuple
from typing import List


Sector = namedtuple('Sector', 'start end')
Group = namedtuple('Group', 'first second')


def parse_sector(text):
    points = list(map(int, text.split('-')))
    return Sector(points[0], points[1])


def parse_groups(file) -> List[Group]:
    lines = [line.strip() for line in file.readlines()]
    groups = []
    for line in lines:
        sectors = [parse_sector(sector) for sector in line.split(',')]
        groups.append(Group(sectors[0], sectors[1]))
    return groups


def part1():
    with open('day_4_part_1_input.txt') as file:
        groups = parse_groups(file)
    
    answer = 0
    for group in groups:
        first = group.first
        second = group.second
        if first.start <= second.start and first.end >= second.end \
                or second.start <= first.start and second.end >= first.end:
            answer += 1
    print(answer)


def part2():
    with open('day_4_part_2_input.txt') as file:
        groups = parse_groups(file)
    
    answer = 0
    for group in groups:
        first = group.first
        second = group.second
        if not (first.end < second.start or second.end < first.start):
            answer += 1
    print(answer)


if __name__ == "__main__":
    part1()
    part2()