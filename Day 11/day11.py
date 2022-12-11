def part1(fileName):
    class Monkey:
        def __init__(self, objList, operation, test, tThrow, fThrow) -> None:
            self.objList = objList
            self.operation = operation.strip()
            self.test = test.strip()
            self.tThrow = tThrow.strip()
            self.fThrow = fThrow.strip()
            self.inspect = 0

        def __str__(self) -> str:
            return f"Monkey with list {self.objList} and {self.test, self.tThrow, self.fThrow}"

    f = open(fileName).read().split("\n\n")
    for blockIdx in range(len(f)):
        f[blockIdx] = f[blockIdx].split("\n")
    monkeyList = [
        Monkey(
            list(map(int, i[1].strip().split(":")[1].split(","))),
            i[2],
            i[3],
            i[4],
            i[5],
        )
        for i in f
    ]
    for _ in range(20):
        for i in monkeyList:
            while i.objList:
                old = i.objList[0]
                i.objList[0] = eval(i.operation.split("=")[1])
                test = int(i.objList[0]) // 3 % eval(i.test.split(" ")[-1]) == 0
                if test:
                    monkeyList[int(i.tThrow[-1])].objList.append(i.objList[0] // 3)
                else:
                    monkeyList[int(i.fThrow[-1])].objList.append(i.objList[0] // 3)
                i.objList.pop(0)
                i.inspect += 1
    inspectList = list(sorted([i.inspect for i in monkeyList]))
    return inspectList[-1] * inspectList[-2]


def part2(fileName):
    
    
    monkeyList = []
    f = open(fileName).read().strip().split("\n\n")
    for i in f:
        lines = i.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeyList.append(monkey)

    
    lengths = [0 for _ in range(len(monkeyList))]
    
    
    mod = 1
    for monkey in monkeyList:
        mod *= monkey[2]

    
    for _ in range(10000):
        for index, monkey in enumerate(monkeyList):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= mod
                if item % monkey[2] == 0:
                    monkeyList[monkey[3]][0].append(item)
                else:
                    monkeyList[monkey[4]][0].append(item)
            lengths[index] += len(monkey[0])
            monkey[0] = []

    lengths.sort()
    return (lengths[-1] * lengths[-2])
if __name__ == "__main__":
    import os

    print(
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
