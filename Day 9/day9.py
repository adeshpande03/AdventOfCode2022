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
    return 0


if __name__ == "__main__":
    import os

    print(
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
