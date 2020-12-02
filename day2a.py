def main():
    with open('input2.txt') as f:
        lines = [line.rstrip() for line in f]

    pw_count = 0

    for line in lines:
        line_split = line.split(" ")
        pw = line_split[2]
        letter = line_split[1][0]

        pos_1 = int(line_split[0].split("-")[0]) - 1
        pos_2 = int(line_split[0].split("-")[1]) - 1

        if (pw[pos_1] is letter or pw[pos_2] is letter) and not (pw[pos_1] is letter and pw[pos_2] is letter):
            pw_count += 1

    print(pw_count)


if __name__ == "__main__":
    main()
