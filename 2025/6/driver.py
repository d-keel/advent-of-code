#!/bin/python3

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def stripLines(lines: list[str]) -> list[list[str]]:
    newLines: list[list[str]] = []

    for line in lines:
        newLines.append(line.split())

    return newLines

def convertMatrix(matrix: list[list[str]]) -> list[list[str]]:
    newMatrix: list[list[str]] = []

    for col in range(len(matrix[0])):
        curCol: list[str] = []
        for row in range(len(matrix)):
            val: str = ''
            val = matrix[row][col]
            curCol.append(val)
        newMatrix.append(curCol)

    return newMatrix
    
def solveLines(lines: list[list[str]]) -> int:
    nums: list[list[int]] = []
    ops: list[str] = []
    operations: list[str] = ['*', '+']
    solved: list[int] = []

    for row in lines:
        curRow: list[int] = []
        for val in row:
            if val in operations:
                ops.append(val)
            else:
                curRow.append(int(val))
        nums.append(curRow)

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
    lines: list[str] = readFile('given.txt')
    count: int = 0
    count2: int = 0
    matrix: list[list[str]] = convertMatrix(stripLines(lines))

    count = solveLines(matrix)

    print("Part 1:", count)
    print("Part 2:", count2)


if __name__ == "__main__":
    main()
