def main():
    with open('input3.txt') as f:
        lines = [line.rstrip() for line in f]
    print(travel(lines, 3, 1))
    print(travel(lines, 1, 1) * travel(lines, 3, 1) * travel(lines, 5, 1) * travel(lines, 7, 1) * travel(lines, 1, 2))


def travel(lines, right, down):
    trees, column = 0, 0
    for i in range(0, len(lines), down):
        line = lines[i]
        if line[column % len(line)] == '#':
            trees += 1
        column += right
    return trees


if __name__ == "__main__":
    main()
