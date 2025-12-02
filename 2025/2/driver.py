#!/bin/python3

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().split(',')

    return lines

def rangeCheck(line: str) -> list[int]:
    invalids: list[int] = []
    vals: list[str] = line.split('-')
    for num in range(int(vals[0]), int(vals[1])+1):
        #ignore odd length numbers
        if len(str(num)) % 2:
            continue
        charNum: str = str(num)
        if charNum[len(charNum)//2:] == charNum[:len(charNum)//2]:
            invalids.append(num)
    return invalids

def main():
    lines: list[str] = readFile('sample.txt')
    count: int = 0
    for line in lines:
        invalid = rangeCheck(line)
        for num in invalid:
            count += num

    print("Part 1 Count:", count)

if __name__ == "__main__":
    main()
