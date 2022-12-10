from dataclasses import dataclass

@dataclass
class Command:
    name: str
    argument: str = None


@dataclass
class File:
    name: str
    type: str
    size: int = None


def create_command(tokens):
    name = tokens[1]
    if name == 'cd':
        return Command(name, tokens[2])
    if name == 'ls':
        return Command(name)
    exit(-1)


def create_file(tokens):
    if tokens[0] == 'dir':
        return File(tokens[1], 'd')
    return File(tokens[1], 'f', int(tokens[0]))


def parse_input(file_name):
    with open(file_name) as file:
        line = file.readline()
        data = []
        current_command = None
        while line != '':
            tokens = line.strip().split()
            if tokens[0] == '$':
                current_command = create_command(tokens)
                data.append((current_command, []))
            else:
                data[-1][1].append(create_file(tokens))
            line = file.readline()
    return data


class FileNode:
    def __init__(self, parent=None, childrens=None, info: File = None):
        self.parent = parent
        self.childrens = childrens
        self.info = info

    def __str__(self):
        return f'FileNode(parent={self.parent}, childrens={len(self.childrens)}, info={self.info})'


def build_file_tree(data: list[tuple[Command, list[File]]]):
    tree_root = None
    current_node = None
    
    for command, command_output in data:
        if command.name == 'cd':
            if command.argument == '/':
                tree_root = FileNode(parent=None, childrens=dict(), info=File('/', 'r'))
                current_node = tree_root
            elif command.argument == '..':
                current_node = current_node.parent
            else:
                current_node = current_node.childrens[command.argument]
        elif command.name == 'ls':
            for info in command_output:
                next_node = FileNode(parent=current_node, childrens={}, info=info)
                current_node.childrens[next_node.info.name] = next_node
    return tree_root


def find_dirs_sizes(tree_root):
    dirs_sizes = dict()

    def traverse(node: FileNode):
        dirs_sizes[node] = 0
        for children in node.childrens.values():
            if children.info.type == 'd':
                traverse(children)
                dirs_sizes[node] += dirs_sizes[children]
            else:
                dirs_sizes[node] += children.info.size
    
    traverse(tree_root)
    return dirs_sizes


def part_1(dirs_sizes):
    answer = 0
    for _, size in dirs_sizes.items():
        if size <= 100000:
            answer += size
    print(answer)


def part_2(dirs_sizes, tree_root):
    disc_space = 70000000
    need_to_update = 30000000
    free_space = disc_space - dirs_sizes[tree_root]
    need_to_freeup = need_to_update - free_space

    candidates = [(node, size) for node, size in dirs_sizes.items() if size >= need_to_freeup]
    (_, size) = min(candidates, key=lambda x: x[1])
    print(size)


def main():
    data = parse_input('day_7_input.txt')
    tree_root = build_file_tree(data)
    dirs_sizes = find_dirs_sizes(tree_root)

    part_1(dirs_sizes)
    part_2(dirs_sizes, tree_root)


if __name__ == '__main__':
    main()
