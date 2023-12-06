def part1(fileName):
    file = list(open(fileName))
    cycleNumber = 1
    x = 1
    xList = []
    for f in file:
        if f[0] == "n":
            xList.append((cycleNumber, x))
            cycleNumber += 1
        elif f[0] == "a":
            xList.append((cycleNumber, x))
            cycleNumber += 1
            xList.append((cycleNumber, x))
            cycleNumber += 1
            x += int(f.split(" ")[1])
    if (cycleNumber, x) not in xList:
        xList.append((cycleNumber, x))
    return sum([x[0]*x[1] for x in xList if x[0] in [d * 40 + 20 for d in range(int(xList[-1][0] / 40))]])


def part2(fileName):
    file = list(open(fileName))
    crt = 0
    cycleNumber = 0
    x = 1
    xList = []
    for f in file:
        if f[0] == "n":
            xList.append((cycleNumber, x))
            cycleNumber += 1
        elif f[0] == "a":
            xList.append((cycleNumber, x))
            cycleNumber += 1
            xList.append((cycleNumber, x))
            cycleNumber += 1
            x += int(f.split(" ")[1])
    if (cycleNumber, x) not in xList:
        xList.append((cycleNumber, x))
    litList = [[]]
    for i in xList:
        if i[1] - 1 == crt:
            litList[-1].append(crt)
        elif i[1] == crt:
            litList[-1].append(crt)
        elif i[1] + 1 == crt:
            litList[-1].append(crt)
        crt += 1
        if crt >= 40:
            crt -= 40
            litList.append([])
    totalStr = ''''''
    for i in litList:
        newStr = ''
        for num in range(40):
            if num in i:
                newStr += ('##')
            else:
                newStr += ('..')
        totalStr += newStr + '\n'
    return totalStr[:-1]
        



if __name__ == "__main__":
    import os

    print(
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
