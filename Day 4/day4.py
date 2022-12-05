def part1(fileName):
    return sum(
        [
            (
                int(line.split(",")[0].split("-")[0])
                >= int(line.split(",")[1].split("-")[0])
                and int(line.split(",")[0].split("-")[1])
                <= int(line.split(",")[1].split("-")[1])
            )
            or (
                int(line.split(",")[1].split("-")[0])
                >= int(line.split(",")[0].split("-")[0])
                and int(line.split(",")[1].split("-")[-1])
                <= int(line.split(",")[0].split("-")[-1])
            )
            for line in list(open(fileName, "r"))
            if len(line) > 1
        ]
    )


def part2(fileName):
    return sum(
        [
            not (
                (
                    int(line.split(",")[0].split("-")[1])
                    < int(line.split(",")[1].split("-")[0])
                )
                or (
                    int(line.split(",")[1].split("-")[1])
                    < int(line.split(",")[0].split("-")[0])
                )
            )
            for line in list(open(fileName, "r"))
            if len(line) > 1
        ]
    )


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
    )
