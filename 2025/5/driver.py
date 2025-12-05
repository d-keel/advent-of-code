#!/bin/python3

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def splitLines(lines: list[str]) -> tuple[list[tuple[int,int]],list[int]]:
    fresh: list[tuple[int,int]] = [] 
    available: list[int] = []

    for idx, line in enumerate(lines):
        print(f"Line: {idx+1}/{len(lines)}", end='\r')
        if not line:
            continue
        if '-' in line:
            left, right = line.split('-')
            fresh.append((int(left),int(right)))
        else:
            available.append(int(line))
    print()

    return fresh, available

def checkFresh(fresh: list[tuple[int,int]], ingredient: int) -> bool:
    for (left,right) in fresh:
        if left <= ingredient <= right:
            return True
    return False

def reduceIDRanges(fresh: list[tuple[int,int]]) -> list[tuple[int,int]]:
    freshSorted: list[tuple[int,int]] = sorted(fresh)
    reduced: list[tuple[int,int]] = []

    for low, high in freshSorted:
        if not reduced or low > reduced[-1][1]:
            reduced.append((low,high))
        else:
            reduced[-1] = (reduced[-1][0],max(reduced[-1][1], high))

    return reduced

def totalFreshIDs(fresh: list[tuple[int,int]]) -> int:
    count: int = 0
    for (low, high) in fresh:
        count += (high + 1 - low)

    return count


def main():
    lines: list[str] = readFile('sample.txt')
    count: int = 0
    count2: int = 0

    fresh: list[tuple[int,int]] = []
    available: list[int] = []

    fresh, available = splitLines(lines)
    fresh = reduceIDRanges(fresh)

    for idx, ingredient in enumerate(available):
        print(f"Ingredient: {idx+1}/{len(available)}", end='\r')
        if checkFresh(fresh, ingredient):
            count += 1
    print()
    count2 = totalFreshIDs(fresh)

    print("Part 1:", count)
    print("Part 2:", count2)


if __name__ == "__main__":
    main()
