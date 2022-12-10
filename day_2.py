from enum import Enum


class ShapeType(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RoundResult(Enum):
    WIN_FIRST = 1
    WIN_SECOND = 2
    DRAW = 3


def play_round(first_shape, second_shape):
    if first_shape == second_shape:
        return RoundResult.DRAW

    if first_shape == ShapeType.ROCK:
        if second_shape == ShapeType.PAPER:
            return RoundResult.WIN_SECOND

    if first_shape == ShapeType.PAPER:
        if second_shape == ShapeType.SCISSORS:
            return RoundResult.WIN_SECOND

    if first_shape == ShapeType.SCISSORS:
        if second_shape == ShapeType.ROCK:
            return RoundResult.WIN_SECOND

    return RoundResult.WIN_FIRST


def decode_shape(name):
    mapping = {
        'A': ShapeType.ROCK,
        'B': ShapeType.PAPER, 
        'C': ShapeType.SCISSORS,
        'Y': ShapeType.PAPER,
        'X': ShapeType.ROCK,
        'Z': ShapeType.SCISSORS
    }
    return mapping[name]


def decode_result(name):
    mapping = {
        'Z': RoundResult.WIN_SECOND,
        'X': RoundResult.WIN_FIRST,
        'Y': RoundResult.DRAW,
    }
    return mapping[name]


def find_shape_for_result(first_shape, result):
    shapes = [ShapeType.PAPER, ShapeType.ROCK, ShapeType.SCISSORS]
    for shape in shapes:
        if play_round(first_shape, second_shape = shape) == result:
            return shape


def count_score_for_second_player(first_shape, second_shape):
    def get_result_score(result):
        if result == RoundResult.WIN_FIRST: return 0
        if result == RoundResult.DRAW: return 3
        if result == RoundResult.WIN_SECOND: return 6

    def get_shape_score(shape: ShapeType):
        return shape.value
    
    round_result = play_round(first_shape, second_shape)
    score = get_result_score(round_result)
    score += get_shape_score(second_shape)
    return score


def part_1(rounds):
    final_score = 0
    for round in rounds:
        first_shape = decode_shape(round[0])
        second_shape = decode_shape(round[1])
        final_score += count_score_for_second_player(first_shape, second_shape)

    print(final_score)


def part_2(rounds):
    final_score = 0
    for round in rounds:
        first_shape = decode_shape(round[0])
        result = decode_result(round[1])
        second_shape = find_shape_for_result(first_shape, result)
        final_score += count_score_for_second_player(first_shape, second_shape)

    print(final_score)


def main():
    with open('day_2_input.txt') as file:
        rounds = [line.split() for line in file.readlines()]

    part_1(rounds)
    part_2(rounds)


if __name__ == '__main__':
    main()
