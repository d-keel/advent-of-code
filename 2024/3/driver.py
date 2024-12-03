#!/bin/python3

import re

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def findMul(line: str, pattern: str, parse: bool = True) -> tuple[int, bool]:
    total: int = 0
    matches: list[str] = re.findall(pattern, line)

    for match in matches:
        if match == 'do()':
            parse = True
        elif match == "don't()":
            parse = False
        else:
            if parse:
                num1, num2 = map(int, re.findall(r'\d+', str(match)))
                total += num1 * num2

    return total, parse

def main() -> None:
    lines = readFile('input.txt')
    muls: list[int] = []
    dos: list[int] = []
    mulPattern: str = r'mul\(\d+,\d+\)'
    doPattern: str = rf"{mulPattern}|do\(\)|don't\(\)"
    parse: bool = True

    for line in lines:
        total, _ = findMul(line, mulPattern)
        muls.append(total)
        total, parse = findMul(line, doPattern, parse)
        dos.append(total)

    print(f'Muls: {sum(muls)}\nDos: {sum(dos)}')

if __name__ == '__main__':
    main()
