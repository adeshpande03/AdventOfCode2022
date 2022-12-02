def part1(fileName):
    return sum([{"X": 1, "Y": 2, "Z": 3}.get(line.strip().split()[1]) + (6 if ["X", "Y", "Z"].index(line.strip().split()[1]) - ["A", "B", "C"].index(line.strip().split()[0]) in [1, -2] else 3 if ["X", "Y", "Z"].index(line.strip().split()[1]) - ["A", "B", "C"].index(line.strip().split()[0]) == 0 else 0) for line in open(fileName, "r")])


def part2(fileName):
    return sum([{"X": 1, "Y": 2, "Z": 3}[(["X", "Y", "Z"][["X", "Y", "Z"].index({"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]) - 1] if ["X", "Y", "Z"].index({"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]) > 0 else ["X", "Y", "Z"][2])] if {"X": 0, "Y": 3, "Z": 6}[line.strip().split()[1]] == 0 else {"X": 1, "Y": 2, "Z": 3}[{"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]] if {"X": 0, "Y": 3, "Z": 6}[line.strip().split()[1]] == 3 else {"X": 1, "Y": 2, "Z": 3}[(["X", "Y", "Z"][["X", "Y", "Z"].index({"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]) + 1] if ["X", "Y", "Z"].index({"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]) < 2 else ["X", "Y", "Z"][0])] for line in open(fileName, "r")]) + sum([{"X": 0, "Y": 3, "Z": 6}[line.strip().split()[1]]for line in open(fileName, "r")])
    

if __name__ == "__main__":
    import os
    print(part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"), part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"))
