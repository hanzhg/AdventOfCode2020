def main():
    with open("input12.txt") as f:
        lines = f.read().splitlines()
    o, x, y = 0, 0, 0

    for line in lines:
        instr, val = line[0], int(line[1:])
        if instr == "N":
            y += val
        elif instr == "S":
            y -= val
        elif instr == "E":
            x += val
        elif instr == "W":
            x -= val
        elif instr == "F":
            o = o % 360
            if o == 90:
                y += val
            elif o == 180:
                x -= val
            elif o == 0:
                x += val
            elif o == 270:
                y -= val
        elif instr == "L":
            o += val
        elif instr == "R":
            o += 360 - val

    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
