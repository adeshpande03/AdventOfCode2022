from collections import defaultdict

def part1(fileName):
    visited = set()
    f = list(open(fileName))
    headCoords = [0, 0]
    tailCoords = [0, 0]
    visited.add(tuple(tailCoords))

    def getDifference(headCoords, tailCoords):
        return abs(headCoords[0] - tailCoords[0]) + abs(headCoords[1] - tailCoords[1])

    headDirectionDict = {
        "R": [1, 0],
        "L": [-1, 0],
        "D": [0, -1],
        "U": [0, 1],
    }

    for location in f:
        direction, numSpaces = location.split(" ")
        numSpaces = int(numSpaces.strip())
        for _ in range(numSpaces):
            headCoords[0] += headDirectionDict[direction][0]
            headCoords[1] += headDirectionDict[direction][1]
            tempCoords = (
                headCoords[0] - tailCoords[0],
                headCoords[1] - tailCoords[1],
            )
            if getDifference(headCoords, tailCoords) == 2 and (
                abs(headCoords[0] - tailCoords[0]) > 1
                or abs(headCoords[1] - tailCoords[1]) > 1
            ):
                if tempCoords[0] == 0:
                    if tempCoords[1] < 0:
                        tailCoords[1] -= 1
                    else:
                        tailCoords[1] += 1
                else:
                    if tempCoords[0] < 0:
                        tailCoords[0] -= 1
                    else:
                        tailCoords[0] += 1
                visited.add(tuple(tailCoords))
            elif getDifference(headCoords, tailCoords) == 3:
                if tempCoords[1] > 0 and tempCoords[0] > 0:
                    tailCoords[0] += 1
                    tailCoords[1] += 1
                elif tempCoords[0] < 0 and tempCoords[1] > 0:
                    tailCoords[0] -= 1
                    tailCoords[1] += 1
                elif tempCoords[0] > 0 and tempCoords[1] < 0:
                    tailCoords[0] += 1
                    tailCoords[1] -= 1
                elif tempCoords[0] < 0 and tempCoords[1] < 0:
                    tailCoords[0] -= 1
                    tailCoords[1] -= 1
                visited.add(tuple(tailCoords))
    return len(visited)


def part2(fileName):
    f = list(open(fileName))
    def follow(head, tail):
        rowMove = head[0] - tail[0]
        columnMove = head[1] - tail[1]
        if abs(rowMove) <= 1 and abs(columnMove) <= 1:
            pass
        elif abs(rowMove) >= 2 and abs(columnMove) >= 2:
            tail =((head[0] - 1 if tail[0] < head[0] else head[0] + 1), (head[1] - 1 if tail[1] < head[1] else head[1] + 1))
        elif abs(columnMove) >= 2:
            tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)
        elif abs(rowMove) >= 2:
            tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
        return tail
    head = 0,0
    tailList = [(0, 0) for _ in range(9)]
    print(tailList[8])
    rowDirection = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    columnDirection = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    set1 = set()
    set2 = set()
    set1.add(tailList[0])
    set2.add(tailList[8])
    for location in f:
        direction, numCount = location.split(' ')
        numCount = int(numCount)
        for _ in range(numCount):
            head = (head[0] + rowDirection[direction], head[1]+columnDirection[direction])
            tailList[0] = follow(head, tailList[0])
            for i in range(1, 9):
                tailList[i] = follow(tailList[i-1], tailList[i])
            set1.add(tailList[0])
            set2.add(tailList[8])
    return len(set2)


if __name__ == "__main__":
    import os

    print(
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
