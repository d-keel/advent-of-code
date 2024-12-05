#!/bin/python3

from sys import setrecursionlimit
setrecursionlimit(10**4)

def readFile(filePath: str) -> list[list[str]]:
    lines: list[list[str]] = [[]]

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()
    
    return lines

def cleanGrid(lines: list[str], r: int, c: int, visited: set[tuple[int, int]], count: int, word: str = '') -> int:
    if (r, c) in visited:
        return 0

    visited.add((r,c))

    directions: list[tuple[int, int]] = [(0, 1), (0, -1),   # down up
                                        (1, 0), (-1, 0),    # right left
                                        (-1, -1), (1, 1),   # dUpLeft, dUpRight
                                        (-1, 1), (1, -1)    # dDownRight, dDownLeft
                                        ]

    if (0 <= r < len(lines) and 0 <= c < len(lines[0])):
        if len(word) == 4:
            if word == 'XMAS' or 'SAMX':
                count += 1
            word = ''
        print(r, c, "'", lines[r][c], "'")

        word += lines[r][c]

        for row, col in directions:
            print('DIRECTIONS:', row, col)
            count = cleanGrid(lines, r+row, c+col, visited, count, word)
            if count > 0:
                return count

    return count

def main():
    lines: list[list[str]] = readFile('sample.txt')
    count: int = 0

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            count = cleanGrid(lines, row, col, set(), count)

    print(lines)
    print(count)

if __name__ == '__main__':
    main()