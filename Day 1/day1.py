
# arr = [0]
# index = 0
# for line in inputFile:
#     if len(line) == 1:
#         arr.append(0)
#         index += 1
#     else:
#         arr[index] += int(line.strip())
# print(max(arr))  # Part 1
# print(sum(sorted(arr, reverse=True)[0:3]))  # Part 2

# Part 1 O(n)
def part1(fileName):
    inputFile = open(fileName, "r")
    num, currSum = 0, 0
    for line in inputFile:
        if len(line) == 1:
            num = max(currSum, num)
            currSum = 0
        else:
            currSum += int(line.strip())
    return(num)

# Part 2 O(n)
def part2(fileName):
    inputFile = open(fileName, "r")
    currSum, maxArr = 0, [0, 0, 0]
    for line in inputFile:
        if len(line) == 1:
            maxArr[0] = max(currSum, maxArr[0])
            maxArr, currSum = sorted(maxArr), 0            
        else:
            currSum += int(line.strip())
    return(sum(maxArr))

if __name__ == '__main__':
    import os
    print(part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"), part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"))