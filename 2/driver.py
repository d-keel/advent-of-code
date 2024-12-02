#!/bin/python3

def readFile(filePath: str) -> list[list[int]]:
    lines = list[list[int]]

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    lines = [line.split(' ') for line in lines]
    for i, line in enumerate(lines):
        lines[i] = [int(x) for x in line]

    return lines

def checkSafe(line: list[int]) -> bool:
    increasing: bool = False
    decreasing: bool = False

    for i, v in enumerate(line):
        if i != len(line) - 1:
            val = v - line[i+1]
        else:
            continue
        
        if val < 0:
            increasing = True

        if val > 0:
            decreasing = True

        if increasing and decreasing or not(0 < abs(val) < 4):
            return False

    return True

def checkSafeDampened(line: list[int]) -> bool:
    safe: bool = checkSafe(line)

    if not(safe):
        for i in range(len(line)): 
            temp = line.pop(i)
            safe = checkSafe(line)
            if safe:
                return True
            line.insert(i, temp)

    return safe

def main() -> None:
    lines = readFile('input.txt')
    safe: int = 0
    dampened: int = 0

    for i, line in enumerate(lines):
        if checkSafe(line):
            safe += 1
        if checkSafeDampened(line):
            dampened += 1

    print(f'Safe: {safe}\nDampened: {dampened}')

if __name__ == '__main__':
    main()