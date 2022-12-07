from collections import defaultdict


def part1(fileName):
    currdirectory = {}
    r = {}
    il = []

    for line in open(fileName):
        line = line.strip()
        if line[0] == "$":
            if line[2] == "c":
                directory = line[5:]
                if directory == "/":
                    currdirectory = r
                    il = []

                elif directory == "..":
                    currdirectory = il.pop()

                else:
                    if directory not in currdirectory:
                        currdirectory[directory] = {}
                    il.append(currdirectory)
                    currdirectory = currdirectory[directory]

        else:
            x, y = line.split()
            if x == "dir":
                if y not in currdirectory:
                    currdirectory[y] = {}
            else:
                currdirectory[y] = int(x)

    def compute(r):
        if type(directory) == int:
            return (directory, 0)
        size = 0
        ans = 0

        for child in directory.values():
            s, a = compute(child)
            size += s
            ans += a

        if size <= 100000:
            ans += size
        return (size, ans)

    return compute(r)[1]


def part2(fileName):
    currdirectory = {}
    r = {}
    il = []

    for line in open(fileName):
        line = line.strip()
        if line[0] == "$":
            if line[2] == "c":
                directory = line[5:]
                if directory == "/":
                    currdirectory = r
                    il = []
                elif directory == "..":
                    currdirectory = il.pop()
                else:
                    if directory not in currdirectory:
                        currdirectory[directory] = {}
                    il.append(currdirectory)
                    currdirectory = currdirectory[directory]
        else:
            x, y = line.split()
            if x == "dir":
                if y not in currdirectory:
                    currdirectory[y] = {}
            else:
                currdirectory[y] = int(x)

    def size(directory):
        if type(directory) == int:
            return directory
        return sum(map(size, directory.values()))

    t = size(r) - 40000000

    def solve(directory):
        ans = 1000000000000
        if size(directory) >= t:
            ans = size(directory)
        for child in directory.values():
            if type(child) == int:
                continue
            q = solve(child)
            ans = min(ans, q)
        return ans

    return solve(r)


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dir(os.path.realpath(__file__))}/test.txt"),
        part2(f"{os.path.dir(os.path.realpath(__file__))}/test.txt"),
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
