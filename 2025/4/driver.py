#!/bin/python3
from typing import Tuple

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def checkValid(lines: list[str], maxNeighbors: int) -> tuple[int, list[tuple[int,int]]]:
    valids: int = 0
    directions: list[tuple[int, int]] = [
                                         (-1, -1)   ,
                                         (-1,  0)   ,
                                         (-1,  1)   ,
                                         ( 0, -1)   ,
                                         ( 0,  1)   ,
                                         ( 1, -1)   ,
                                         ( 1,  0)   ,
                                         ( 1,  1)
                                        ]
    locations: list[tuple[int, int]] = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '@':
                foundNeighbors: int = 0
                if (0 <= row < len(lines) and 0 <= col < len(lines[row])) and lines[row][col] == '@':
                    for roww, coll in directions:
                        if (row + roww > len(lines)-1)\
                        or (col+coll > len(lines)-1)\
                        or (row+roww < 0)\
                        or (col+coll < 0):
                            #print("Out of bounds")
                            continue
                        if lines[row + roww][col + coll] == '@':
                            #print("Currently on row, col:", row, col)
                            #print("Found neighbor at row, col:", row+roww, col+coll)
                            #print(lines[row+roww])
                            foundNeighbors += 1
                if foundNeighbors < maxNeighbors:
                    locations.append((row,col))
                    valids += 1
                #print("-----STATE------")
                #print(*lines, sep='\n')
                #print("Neighbors: ", foundNeighbors, "At row,col:", row, col)
                #print(locations)
                #print("-----STATE------")

    return valids, locations

def showLocations(lines: list[str], locations: list[tuple[int, int]]):
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (row, col) in locations:
                print("\033[92m"+lines[row][col]+"\033[0m", end='')
            else:
                print(lines[row][col], end='')
        print()


def main():
    lines: list[str] = readFile('sample.txt')
    count: int = 0
    count2: int = 0

    count, locations = checkValid(lines, 4)
    showLocations(lines, locations)
    #count2 += int()


    print("Part 1:", count)
    print("Part 2:", count2)


if __name__ == "__main__":
    main()
