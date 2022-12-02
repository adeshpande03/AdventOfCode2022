def part1(fileName):
    return sum([{"X": 1, "Y": 2, "Z": 3}.get(line.strip().split()[1]) + (6 if ["X", "Y", "Z"].index(line.strip().split()[1]) - ["A", "B", "C"].index(line.strip().split()[0]) in [1, -2] else 3 if ["X", "Y", "Z"].index(line.strip().split()[1]) - ["A", "B", "C"].index(line.strip().split()[0]) == 0 else 0) for line in open(fileName, "r")])


def part2(filename):
    f = open(filename, "r")
    oppPossible = ["X", "Y", "Z"]
    resultKey = {"X": 0, "Y": 3, "Z": 6}
    choiceKey = {"X": 1, "Y": 2, "Z": 3}
    matchingOppToMe = {"A": "X", "B": "Y", "C": "Z"}

    def pickMe(opponent, result):
        if result == 0:
            myChoice = (
                oppPossible[oppPossible.index(opponent) - 1]
                if oppPossible.index(opponent) > 0
                else oppPossible[2]
            )
        elif result == 3:
            myChoice = opponent
        elif result == 6:
            myChoice = (
                oppPossible[oppPossible.index(opponent) + 1]
                if oppPossible.index(opponent) < 2
                else oppPossible[0]
            )
        return choiceKey[myChoice]

    return sum(
        [
            pickMe(
                matchingOppToMe[line.strip().split()[0]],
                resultKey[line.strip().split()[1]],
            )
            + resultKey[line.strip().split()[1]]
            for line in f
        ]
    )


if __name__ == "__main__":
    print(part1("input.txt"), part2("input.txt"))
