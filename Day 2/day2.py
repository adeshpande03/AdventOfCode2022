def part1(filename):
    key = {"X": 1, "Y": 2, "Z": 3}
    f = open(filename, "r")
    def matchup(opponent, me):
        opponent = ["A", "B", "C"].index(opponent)
        me = ["X", "Y", "Z"].index(me)
        return 6 if me - opponent in [1, -2] else 3 if me - opponent == 0 else 0

    return sum(
        [
            key.get(line.strip().split()[1])
            + matchup(line.strip().split()[0], line.strip().split()[1])
            for line in f
        ]
    )


def part2(filename):
    f = open(filename, "r")
    resultKey = {"X": 0, "Y": 3, "Z": 6}
    choiceKey = {"X": 1, "Y": 2, "Z": 3}
    matchingOppToMe = {"A": "X", "B": "Y", "C": "Z"}

    def pickMe(opponent, result):
        oppPossible = ["X", "Y", "Z"]
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
