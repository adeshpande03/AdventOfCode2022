def part1(filename):
    pointTotal = 0
    key = {"X": 1, "Y": 2, "Z": 3}

    def matchup(opponent, me):
        oppPossible = ["A", "B", "C"]
        mePossible = ["X", "Y", "Z"]
        opponent = oppPossible.index(opponent)
        me = mePossible.index(me)
        if me - opponent in [1, -2]:
            return 6
        elif me - opponent == 0:
            return 3
        else:
            return 0

    f = open(filename, "r")
    for line in f:
        line = line.strip().split()
        pointTotal += key.get(line[1]) + matchup(line[0], line[1])
    return pointTotal


def part2(filename):
    f = open(filename, "r")
    pointTotal = 0
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
            return choiceKey[myChoice]
        if result == 3:
            return choiceKey[opponent]
        if result == 6:
            myChoice = (
                oppPossible[oppPossible.index(opponent) + 1]
                if oppPossible.index(opponent) < 2
                else oppPossible[0]
            )
            return choiceKey[myChoice]

    for line in f:
        line = line.strip().split()
        pointTotal += (
            pickMe(matchingOppToMe[line[0]], resultKey[line[1]]) + resultKey[line[1]]
        )
    return pointTotal


if __name__ == "__main__":
    print(part1("input.txt"), part2("input.txt"))
