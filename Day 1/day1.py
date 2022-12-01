import os
print(os.listdir())
inputFile = open("input.txt", "r")
arr = [0]
index = 0
for line in inputFile:
    if len(line) == 1:
        arr.append(0)
        index += 1
    else:
        arr[index] += int(line.strip())
print(sum(sorted(arr, reverse = True)[0:3]))
