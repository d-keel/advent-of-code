#!/bin/python3

import re

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def findMul(line: str) -> int:
    total: int = 0
    pattern: str = r'mul\(\d+,\d+\)'
    digitPattern: str = r'\d+'
    matches: list[str] = re.findall(pattern, line)

    for match in matches:
        num1, num2 = re.findall(digitPattern, match)
        num1, num2 = int(num1), int(num2)
        total += (num1 * num2)

    return total

def findDoMul(line: str) -> int:
    total: int = 0
    pattern: str = r'mul\(\d+,\d+\)'
    aroundDo: str = r"(.*?)(?=don't\(\))|(?<=do\(\))(.*?)(?=don't\(\)|$)"
    digitPattern: str = r'\d+'
    chunks: list[str] = re.findall(aroundDo, line)

    for chunk in chunks:
        mulMatch: list[str] = re.findall(pattern, str(chunk))
        for match in mulMatch:
            num1, num2 = re.findall(digitPattern, match)
            num1, num2 = int(num1), int(num2)
            total += (num1 * num2)

    return total

def main() -> None:
    lines = readFile('input.txt')
    muls: list[int] = []
    dos: list[int] = []
    for line in lines:
        muls.append(findMul(line))
        dos.append(findDoMul(line))

    #ans < 147910205

    print(f'Muls: {sum(muls)}\nDos: {sum(dos)}')

if __name__ == '__main__':
    main()
