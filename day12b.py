def main():
    with open("input12.txt") as f:
        lines = f.read().splitlines()
    o, x, y = 0, 0, 0
    x2, y2 = 10, 1

    def rotate(x, y, val):
        if val == 0:
            return x, y
        elif val == 90:
            return -y, x
        elif val == 180:
            return -x, -y
        elif val == 270:
            return y, -x

    for line in lines:
        instr, val = line[0], int(line[1:])
        if instr == "N":
            y2 += val
        elif instr == "S":
            y2 -= val
        elif instr == "E":
            x2 += val
        elif instr == "W":
            x2 -= val
        elif instr == "F":
            x += val * x2
            y += val * y2
        elif instr == "L":
            x2, y2 = rotate(x2, y2, val)
        elif instr == "R":
            x2, y2 = rotate(x2, y2, 360 - val)

    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
