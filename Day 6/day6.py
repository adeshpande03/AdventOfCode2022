def part1(fileName):

    return (
        next(
            (
                index
                for index, value in enumerate(
                    [
                        i if len(set(open(fileName).readline()[i : i + 4])) == 4 else 0
                        for i in range(len(open(fileName).readline()))
                    ]
                )
                if value != 0
            ),
            None,
        )
        + 4
    )
    f = open(fileName).readline()
    for i in range(0, len(f)):
        if len(set(f[i : i + 4])) == 4:
            return i + 4


def part2(fileName):
    return (
        next(
            (
                index
                for index, value in enumerate(
                    [
                        i
                        if len(set(open(fileName).readline()[i : i + 14])) == 14
                        else 0
                        for i in range(len(open(fileName).readline()))
                    ]
                )
                if value != 0
            ),
            None,
        )
        + 14
    )
    f = open(fileName).readline()
    for i in range(0, len(f)):
        if len(set(f[i : i + 14])) == 14:
            return i + 14


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
