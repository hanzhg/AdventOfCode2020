def main():
    with open('input5.txt') as f:
        lines = f.read().splitlines()

    array = []

    for line in lines:
        array.append(int(line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2))

    # part 1
    print(max(array))

    # part 2
    for line in range(min(array), max(array)):
        if line not in array:
            print(line)


if __name__ == "__main__":
    main()
