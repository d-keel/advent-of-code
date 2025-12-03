#!/bin/python3

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def findJoltage(line: str) -> tuple[int, int, int]:
    joltage: str = '00'
    left: int = 0
    right: int = len(line) - 1
    lastSetLeft: int = 0
    lastSetRight: int = 0

    while left < right:
        if int(line[left]) > int(joltage[0]):
            joltage = str(line[left]) + str(line[right])
            lastSetLeft = left
        if int(line[right]) > int(joltage[1]):
            joltage = str(line[left]) + str(line[right])
            lastSetRight = right
        if line[left] > line[right]: 
            right -= 1
        #else the right value is greater than the left value
        #and right is not the end of the line
        #and has right passed the mid point of the line
        elif line[right] >= line[left] and right != len(line) - 1 and right < len(line) // 2:
            #print("Old left right", left, right)
            left = right
            right = len(line) - 1
            #print("New left right", left, right)
        else:
            #print("moving left")
            left += 1
    #print("Joltage:", joltage,"\nLeft:", lastSetLeft, "Right:", lastSetRight)
    
    return int(joltage), lastSetLeft, lastSetRight

def findJoltage2(line: list[int]) -> str:
    maxx: int = max(line[:-1])
    pos: int = line.index(maxx)
    nMax: int = max(line[pos+1:])
    return str(maxx) + str(nMax)

def findBiggerJoltage(line: list[int]) -> str:
    stack: list[int] = []
    sz: int = len(line)
    joltage: str = ""

    for i, v in enumerate(line):
        while stack and stack[-1] < v and len(stack) + (sz - i) > 12:
            _ = stack.pop()
        if len(stack) < 12:
            stack.append(v)
   
    for num in stack:
        joltage += str(num)

    return joltage


def main():
    lines: list[str] = readFile('sample.txt')
    count: int = 0
    count2: int = 0

    for line in lines:
        count += int(findJoltage2(line))
        count2 += int(findBiggerJoltage(line))


    print("Part 1:", count)
    print("Part 2:", count2)


if __name__ == "__main__":
    main()
