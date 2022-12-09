


def part1(fileName):
    return 0
def part2(fileName):
    return 0

if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
