input_name = 'day_1_input.txt'

with open(input_name) as file_input:
    lines = [line.strip() for line in file_input.readlines()]
data = [[]]
for line in lines:
    if line == "":
        data.append([])
    else:
        data[len(data) - 1].append(int(line))

sums = list(map(sum, data))

# part1
most = max(sums)
print(most)

# part2
most_3 = sum(sorted(sums)[-3:])
print(most_3)
