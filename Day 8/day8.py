


def part1(fileName):
    c = 0
    treeList = [list(treeRow.strip()) for treeRow in list(open(fileName))]

    def checkHorizontal(treeList, i, j):
        h1List = list(range(0, j))
        h2List = list(range(j + 1, len(treeList[0])))
        return all(treeList[i][hCoord] < treeList[i][j] for hCoord in h1List) or all(
            treeList[i][hCoord] < treeList[i][j] for hCoord in h2List
        )

    def checkVertical(treeList, i, j):
        v1List = list(range(0, i))
        v2List = list(range(i + 1, len(treeList)))
        return all(treeList[vCoord][j] < treeList[i][j] for vCoord in v1List) or all(
            treeList[vCoord][j] < treeList[i][j] for vCoord in v2List
        )

    def valid(treeList, i, j):
        return checkVertical(treeList, i, j) or checkHorizontal(treeList, i, j)

    for i in range(len(treeList)):
        for j in range(len(treeList[i])):
            if valid(treeList, i, j):
                c += 1
    return c


def part2(fileName):
    treeList = [list(treeRow.strip()) for treeRow in list(open(fileName))]

    def countHorizontal(treeList, i, j):
        c1, c2 = 0, 0
        h1List = list(reversed(range(0, j)))
        h2List = list((range(j + 1, len(treeList[0]))))

        for h in h1List:
            if treeList[i][h] < treeList[i][j]:
                c1 += 1
            else:
                c1 += 1
                break
        for h in h2List:
            if treeList[i][h] < treeList[i][j]:
                c2 += 1
            else:
                c2 += 1
                break
        return c1 * c2

    def countVertical(treeList, i, j):
        c1, c2 = 0, 0
        v1List = list(reversed(range(0, i)))
        v2List = list((range(i + 1, len(treeList))))
        for v in v1List:
            if treeList[v][j] < treeList[i][j]:
                c1 += 1
            else:
                c1 += 1
                break
        for v in v2List:
            if treeList[v][j] < treeList[i][j]:
                c2 += 1
            else:
                c2 += 1
                break
        return c1 * c2
    maxMum = -1
    for i in range(1, len(treeList) - 1):
        for j in range(1, len(treeList[0]) - 1):
            maxMum = max(
                countHorizontal(treeList, i, j) * countVertical(treeList, i, j), maxMum
            )
    return maxMum


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
