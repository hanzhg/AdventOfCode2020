def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    result = 0

    for line in lines:
        for line1 in lines:
            value1 = 2020 - (int(line) + int(line1))
            if str(value1) in lines:
                result = int(line) * int(line1) * value1

    print(result)


if __name__ == "__main__":
    main()
