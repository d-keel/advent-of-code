#!/bin/python3

def readFile(filePath: str) -> list[list[str]]:
    lines: list[list[str]] = []

    with open(filePath, 'r') as f:
        #lines = f.read().splitlines()
        for line in f:
            lines.append(line.split())

    return lines

def solveLines(lines: list[list[str]]) -> int:
    numRows: int = len(lines)
    numCols: int = len(lines[0])
    nums: list[list[int]] = []
    ops: list[str] = []
    operations: list[str] = ['*', '/', '+', '-']
    solved: list[int] = []

    for col in range(numCols):
        curCol: list[int] = []
        for row in range(numRows):
            val: str = ''
            val = lines[row][col]
            if val in operations:
                ops.append(val)
            else:
                curCol.append(int(val))
        nums.append(curCol)

    for idx, op in enumerate(ops):
        total: int = 0
        if op == '*':
            total = 1
            for num in nums[idx]:
                total *= num
        if op == '+':
            for num in nums[idx]:
                total += num
        solved.append(total)
        
    return sum(solved)

def main():
    lines: list[list[str]] = readFile('given.txt')
    count: int = 0
    count2: int = 0

    count = solveLines(lines)


    print("Part 1:", count)
    print("Part 2:", count2)


if __name__ == "__main__":
    main()
