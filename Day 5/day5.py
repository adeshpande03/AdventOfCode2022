def part1(fileName):
    f = list(open(fileName, "r"))
    boxList = []
    idx = f.index("\n")
    for i in range(idx - 1):
        boxList.append(f[i])
    indices = [f[idx - 1].index(d) for d in f[idx - 1] if d.isdigit()]
    boxVals = []
    for row in boxList:
        boxVals.append([row[index] for index in indices])
    boxVals = list(zip(*boxVals))
    boxVals = [list(i) for i in boxVals]
    for row in range(len(boxVals)):
        while " " in boxVals[row]:
            boxVals[row].remove(" ")
    boxVals = [list(reversed(i)) for i in boxVals]

    for i in range(idx + 1, len(f)):
        line = f[i].split()
        number, takeFrom, addTo = (int(line[1]), int(line[3]) - 1, int(line[5]) - 1)
        for i in range(number):
            boxVals[addTo] += boxVals[takeFrom].pop()

    return "".join([i[-1] for i in boxVals])


def part2(fileName):
    f = list(open(fileName, "r"))
    boxList = []
    idx = f.index("\n")
    for i in range(idx - 1):
        boxList.append(f[i])
    indices = [f[idx - 1].index(d) for d in f[idx - 1] if d.isdigit()]
    boxVals = []
    for row in boxList:
        boxVals.append([row[index] for index in indices])
    boxVals = list(zip(*boxVals))
    boxVals = [list(i) for i in boxVals]

    for row in range(len(boxVals)):
        while " " in boxVals[row]:
            boxVals[row].remove(" ")
    boxVals = [list(reversed(i)) for i in boxVals]

    for i in range(idx + 1, len(f)):
        line = f[i].split()
        number, takeFrom, addTo = (int(line[1]), int(line[3]) - 1, int(line[5]) - 1)
        moveList = []
        for i in range(number):
            moveList.append(boxVals[takeFrom].pop())
        boxVals[addTo] += reversed(moveList)

    return "".join([i[-1] for i in boxVals])


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep = "\n"
    )
