def part1(fileName):
    return sum(
        [
            ord(
                list(
                    set(line[len(line) // 2 :]).intersection(
                        set(line[0 : len(line) // 2])
                    )
                )[0]
            )
            - 38
            if list(
                set(line[len(line) // 2 :]).intersection(set(line[0 : len(line) // 2]))
            )[0].isupper()
            else ord(
                list(
                    set(line[len(line) // 2 :]).intersection(
                        set(line[0 : len(line) // 2])
                    )
                )[0]
            )
            - 96
            for line in open(fileName, "r")
        ]
    )


def part2(fileName):
    return sum(
        [
            ord(
                list(
                    set(list(open(fileName, "r"))[idx].strip())
                    .intersection(set(list(open(fileName, "r"))[idx + 1]))
                    .intersection(set(list(open(fileName, "r"))[idx + 2]))
                )[0]
            )
            - 38
            if list(
                set(list(open(fileName, "r"))[idx].strip())
                .intersection(set(list(open(fileName, "r"))[idx + 1]))
                .intersection(set(list(open(fileName, "r"))[idx + 2]))
            )[0].isupper()
            else ord(
                list(
                    set(list(open(fileName, "r"))[idx].strip())
                    .intersection(set(list(open(fileName, "r"))[idx + 1]))
                    .intersection(set(list(open(fileName, "r"))[idx + 2]))
                )[0]
            )
            - 96
            for idx in range(0, len(list(open(fileName, "r"))), 3)
        ]
    )


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
    )
