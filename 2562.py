import sys

maxIndex = 0

for i in range(9):
    value = int(sys.stdin.readline())
    if i == 0:
        maxValue = value
        maxIndex = 1
    else:
        if maxValue < value:
            maxIndex = i+1
            maxValue = value

print(maxValue)
print(maxIndex)