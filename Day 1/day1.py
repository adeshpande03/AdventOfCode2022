inputFile = open("input.txt", "r")
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
def part1():
    num, currSum = 0, 0
    for line in inputFile:
        if len(line) == 1:
            num = max(currSum, num)
            currSum = 0
        else:
            currSum += int(line.strip())
    print(num)

# Part 2 O(n)
def part2():
    currSum, maxArr = 0, [0, 0, 0]
    for line in inputFile:
        if len(line) == 1:
            currSum, maxArr[maxArr.index(min(maxArr))] = 0, max(currSum, min(maxArr))
        else:
            currSum += int(line.strip())
    print(sum(maxArr))
