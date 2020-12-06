def main():
    with open('input6.txt') as f:
        lines = f.read().split("\n\n")

    count = 0
    count2 = 0

    for line in lines:
        count += len(list(set(line.replace("\n", ""))))
        count2 += len(set.intersection(*map(set, line.split("\n"))))

    # part 1
    print(count)

    # part 2
    print(count2)


if __name__ == "__main__":
    main()
