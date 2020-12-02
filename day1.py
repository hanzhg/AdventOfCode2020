def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    result = 0

    for line in lines:
        value = 2020 - int(line)
        if str(value) in lines:
            result = int(line) * value

    print(result)


if __name__ == "__main__":
    main()
