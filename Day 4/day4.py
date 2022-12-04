def part1():
    f = list(open("input.txt", "r"))
    il = []
    for line in f:
        line = line.strip()
        if line:
            line = line.split(",")
            line0 = line[0]
            line1 = line[1]
            line0 = list(range((int(line0.split("-")[0])), (int(line0.split("-")[1]) + 1)))
            line1 = list(range((int(line1.split("-")[0])), (int(line1.split("-")[1]) + 1)))
            il.append(line0)
            il.append(line1)
    c = 0
    for i in range(0, len(il), 2):
        if (len(set(il[i + 1]).intersection(set(il[i]))) < len(il[i+ 1]) or len(set(il[i + 1]).intersection(set(il[i]))) < len(il[i]) ):
            c += 1
    print(c)

def part2():
    f = list(open("input.txt", "r"))
    il = []
    for line in f:
        line = line.strip()
        if line:
            line = line.split(",")
            line0 = line[0]
            line1 = line[1]
            line0 = list(range((int(line0.split("-")[0])), (int(line0.split("-")[1]) + 1)))
            line1 = list(range((int(line1.split("-")[0])), (int(line1.split("-")[1]) + 1)))
            il.append(line0)
            il.append(line1)
    c = 0
    for i in range(0, len(il), 2):
        if (len(set(il[i + 1]).intersection(set(il[i]))) > 0):
            c += 1
    print(c)
part2()