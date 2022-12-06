def part1(fileName):
    return sum(
        [
            {"X": 1, "Y": 2, "Z": 3}.get(line.strip().split()[1])
            + (
                6
                if ["X", "Y", "Z"].index(line.strip().split()[1])
                - ["A", "B", "C"].index(line.strip().split()[0])
                in [1, -2]
                else 3
                if ["X", "Y", "Z"].index(line.strip().split()[1])
                - ["A", "B", "C"].index(line.strip().split()[0])
                == 0
                else 0
            )
            for line in open(fileName, "r")
        ]
    )
    
    # key = {"X": 1, "Y": 2, "Z": 3}
    # f = open(filename, "r")

    # def matchup(opponent, me):
    #     opponent = ["A", "B", "C"].index(opponent)
    #     me = ["X", "Y", "Z"].index(me)
    #     return 6 if me - opponent in [1, -2] else 3 if me - opponent == 0 else 0

    # return sum(
    #     [
    #         key.get(line.strip().split()[1])
    #         + matchup(line.strip().split()[0], line.strip().split()[1])
    #         for line in f
    #     ]
    # )



def part2(fileName):
    return sum(
        [
            {"X": 1, "Y": 2, "Z": 3}[
                (
                    ["X", "Y", "Z"][
                        ["X", "Y", "Z"].index(
                            {"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]
                        )
                        - 1
                    ]
                    if ["X", "Y", "Z"].index(
                        {"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]
                    )
                    > 0
                    else ["X", "Y", "Z"][2]
                )
            ]
            if {"X": 0, "Y": 3, "Z": 6}[line.strip().split()[1]] == 0
            else {"X": 1, "Y": 2, "Z": 3}[
                {"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]
            ]
            if {"X": 0, "Y": 3, "Z": 6}[line.strip().split()[1]] == 3
            else {"X": 1, "Y": 2, "Z": 3}[
                (
                    ["X", "Y", "Z"][
                        ["X", "Y", "Z"].index(
                            {"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]
                        )
                        + 1
                    ]
                    if ["X", "Y", "Z"].index(
                        {"A": "X", "B": "Y", "C": "Z"}[line.strip().split()[0]]
                    )
                    < 2
                    else ["X", "Y", "Z"][0]
                )
            ]
            for line in open(fileName, "r")
        ]
        + [
            {"X": 0, "Y": 3, "Z": 6}[line.strip().split()[1]]
            for line in open(fileName, "r")
        ]
    )

    # f = open(filename, "r")
    # oppPossible = ["X", "Y", "Z"]
    # resultKey = {"X": 0, "Y": 3, "Z": 6}
    # choiceKey = {"X": 1, "Y": 2, "Z": 3}
    # matchingOppToMe = {"A": "X", "B": "Y", "C": "Z"}

    # def pickMe(opponent, result):
    #     if result == 0:
    #         myChoice = (
    #             oppPossible[oppPossible.index(opponent) - 1]
    #             if oppPossible.index(opponent) > 0
    #             else oppPossible[2]
    #         )
    #     elif result == 3:
    #         myChoice = opponent
    #     elif result == 6:
    #         myChoice = (
    #             oppPossible[oppPossible.index(opponent) + 1]
    #             if oppPossible.index(opponent) < 2
    #             else oppPossible[0]
    #         )
    #     return choiceKey[myChoice]

    # return sum(
    #     [
    #         pickMe(
    #             matchingOppToMe[line.strip().split()[0]],
    #             resultKey[line.strip().split()[1]],
    #         )
    #         + resultKey[line.strip().split()[1]]
    #         for line in f
    #     ]
    # )
    
    
if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
    )
