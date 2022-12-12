from collections import deque


def part1(fileName):
    f = open(fileName).read().strip()
    lines = [x for x in f.split("\n")]

    grid = []
    for line in lines:
        grid.append(line)
    gridLen = len(grid)
    C = len(grid[0])

    E = [[0 for _ in range(C)] for _ in range(gridLen)]
    for r in range(gridLen):
        for c in range(C):
            if grid[r][c] == "S":
                E[r][c] = 1
            elif grid[r][c] == "E":
                E[r][c] = 26
            else:
                E[r][c] = ord(grid[r][c]) - ord("a") + 1

    def bfs():
        Q = deque()
        for r in range(gridLen):
            for c in range(C):
                if grid[r][c] == "S":
                    Q.append(((r, c), 0))

        S = set()
        while Q:
            (r, c), d = Q.popleft()
            if (r, c) in S:
                continue
            S.add((r, c))
            if grid[r][c] == "E":
                return d
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < gridLen and 0 <= cc < C and E[rr][cc] <= 1 + E[r][c]:
                    Q.append(((rr, cc), d + 1))

    return bfs()


def part2(fileName):
    f = open(fileName).read().strip()
    lines = [x for x in f.split("\n")]

    grid = []
    for line in lines:
        grid.append(line)
    gridLen = len(grid)
    C = len(grid[0])

    E = [[0 for _ in range(C)] for _ in range(gridLen)]
    for r in range(gridLen):
        for c in range(C):
            if grid[r][c] == "S":
                E[r][c] = 1
            elif grid[r][c] == "E":
                E[r][c] = 26
            else:
                E[r][c] = ord(grid[r][c]) - ord("a") + 1

    def bfs():
        Q = deque()
        for r in range(gridLen):
            for c in range(C):
                if E[r][c] == 1:
                    Q.append(((r, c), 0))

        S = set()
        while Q:
            (r, c), d = Q.popleft()
            if (r, c) in S:
                continue
            S.add((r, c))
            if grid[r][c] == "E":
                return d
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < gridLen and 0 <= cc < C and E[rr][cc] <= 1 + E[r][c]:
                    Q.append(((rr, cc), d + 1))

    return bfs()


if __name__ == "__main__":
    import os

    print(
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
