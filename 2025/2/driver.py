#!/bin/python3

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().split(',')

    return lines

def twiceSequencedCheck(startVal: int, endVal: int) -> list[int]:
    invalids: list[int] = []
    for num in range(startVal, endVal+1):
        chNum: str = str(num)
        if chNum[len(chNum)//2:] == chNum[:len(chNum)//2]:
            invalids.append(num)

    return invalids

def substringCheck(startVal: int, endVal: int) -> list[int]:
    invalids: list[int] = []
    for num in range(startVal, endVal+1):
        chNum: str = str(num)
        for i in range(1, len(chNum)//2 + 1):
            if  len(chNum) % i == 0:
                subStr: str = chNum[:i]
                if subStr * (len(chNum)//i) == chNum:
                    invalids.append(num)
                    break
    return invalids


def main():
    lines: list[str] = readFile('sample.txt')
    count: int = 0
    count2: int = 0

    for line in lines:
        vals: list[str] = line.split('-')
        startVal: int = int(vals[0])
        endVal: int = int(vals[1])

        for num in twiceSequencedCheck(startVal, endVal):
            count += num

        for num in substringCheck(startVal, endVal):
            count2 += num

    print("Part 1 Count:", count)
    print("Part 2 Count:", count2)

if __name__ == "__main__":
    main()
