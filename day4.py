def main():
    with open('test.txt') as f:
        lines = f.read()
    lines = lines.split("\n\n")

    matches = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0

    for line in lines:
        line = line.rstrip("\n")
        if all(x in line for x in matches):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
