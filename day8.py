def main():
    with open("input8.txt") as f:
        lines = f.read().splitlines()

    code = []

    for line in lines:
        code.append(line.split(" "))

    def exe(i, line, result):
        if line[0] == "nop":
            i += 1
            return i, result
        elif line[0] == "acc":
            i += 1
            result += int(line[1])
            return i, result
        elif line[0] == "jmp":
            i += int(line[1])
            return i, result

    def part1(input):
        seen = []
        i = 0
        result = 0
        while i < len(code):
            if i in seen:
                return result, True
            seen.append(i)
            i, result = exe(i, input[i], result)
        return result, False

    def part2(input):
        for i in range(len(code)):
            temp1, temp2 = input[i]
            if temp1 == "acc":
                continue
            elif temp1 == "nop":
                input[i][0] = "jmp"
            elif temp1 == "jmp":
                input[i][0] = "nop"
            result, loop = part1(input)
            if not loop:
                return result
            input[i][0] = temp1

    a, b = part1(code)
    print(a)

    print(part2(code))


if __name__ == '__main__':
    main()
