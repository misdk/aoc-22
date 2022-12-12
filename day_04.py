from collections import namedtuple
from typing import List


Sector = namedtuple('Sector', 'start end')
Group = namedtuple('Group', 'first second')


def parse_sector(text):
    points = list(map(int, text.split('-')))
    return Sector(points[0], points[1])


def parse_groups(file_name) -> List[Group]:
    with open(file_name) as file:
        lines = [line.strip() for line in file.readlines()]
    groups = []
    for line in lines:
        sectors = [parse_sector(sector) for sector in line.split(',')]
        groups.append(Group(sectors[0], sectors[1]))
    return groups


def part_1(groups):    
    answer = 0
    for group in groups:
        first = group.first
        second = group.second
        if first.start <= second.start and first.end >= second.end \
                or second.start <= first.start and second.end >= first.end:
            answer += 1
    print(answer)


def part_2(groups):
    answer = 0
    for group in groups:
        first = group.first
        second = group.second
        if not (first.end < second.start or second.end < first.start):
            answer += 1
    print(answer)


def main():
    groups = parse_groups('day_4_input.txt')
    part_1(groups)
    part_2(groups)


if __name__ == '__main__':
    main()
