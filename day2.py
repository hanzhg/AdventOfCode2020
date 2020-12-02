def main():
    with open('input2.txt') as f:
        lines = [line.rstrip() for line in f]

    pw_count = 0

    for line in lines:
        line_split = line.split(" ")
        pw = line_split[2]
        letter = line_split[1][0]
        count = 0
        for letters in pw:
            if letters is letter:
                count += 1

        lower = int(line_split[0].split("-")[0])
        upper = int(line_split[0].split("-")[1])

        if (count >= lower) and (count <= upper):
            pw_count += 1

    print(pw_count)


if __name__ == "__main__":
    main()
