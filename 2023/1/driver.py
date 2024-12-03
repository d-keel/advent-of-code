#!/bin/python3

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines 

def parseNumbers(lines: list[str]) -> list[str]:
    out: list[str] = []

    for line in lines:
        strr: str = ''
        for ch in line:
            if ch.isdigit():
                strr += ch
        out.append(strr)

    return out

def parseAlphaNumeric(lines: list[str]) -> list[str]:
    out: list[str] = []
    convertDict: dict[str, int] = {
                                     'one': 1,
                                     'two': 2,
                                     'three': 3,
                                     'four': 4,
                                     'five': 5,
                                     'six': 6,
                                     'seven': 7,
                                     'eight': 8,
                                     'nine': 9
                                     }

    for line in lines:
        strr: str = ''
        for i, ch in enumerate(line):
            if ch.isdigit():
                strr += ch
            for key in convertDict.keys():
                if line.startswith(key, i):
                    strr += str(convertDict[key])

        out.append(strr) 

    return out


def makeTwoDigit(lines: list[str]) -> list[int]:
    out: list[int] = []

    for line in lines:
        strr: str = ''
        if len(line) >= 2:
            strr = line[0] + line[-1]
        else:
            strr = line[0] + line[0]
        out.append(int(strr))

    return out


def main() -> None:
    #Part 1
    rawLines = readFile('input.txt')
    lines = parseNumbers(rawLines)
    lines = makeTwoDigit(lines)
    print(sum(lines))
    #Part 2
    lines = parseAlphaNumeric(rawLines)
    lines = makeTwoDigit(lines)
    print(sum(lines))



if __name__ == '__main__':
    main()
