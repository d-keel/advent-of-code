#!/bin/python3

def readFile(filePath: str) -> list[int]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
       lines = f.read().splitlines()

    grid: list[list[str]] = [[' ' for _ in range(len(lines[0]))] for _ in range(len(lines))]

    for r in range(len(lines[0])):
        for c in range(len(lines[r])):
            grid[r][c] = lines[r][c]

    #search the grid for adjacent symbols to digits,
    #add the numbers to connected
    connected = search(grid)

    return connected

def DFS(grid: list[list[str]], r: int, c: int, visited: set[tuple[int, int]])-> bool:
    directions: list[tuple[int, int]] = [(0,1), (0,-1), (1,0), (-1,0)]
    valid: bool = False
    if len(visited) == 0:
        visited = set()
    ch: str = grid[r][c]

    if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited) and ch.isdigit():
        valid = True
        visited.add((r, c))
        for rw, cl in directions:
            _ = DFS(grid, r + rw, c + cl, visited)

    return valid

def search(grid: list[list[str]]) -> list[int]:
    connected: list[int] = []

    for r in range(len(grid[0])):
        for c in range(len(grid[r])):
            if DFS(grid, r, c, set()):
                connected.append(int(grid[r][c]))

    return connected

def main() -> None:
    lines = readFile('input.txt')
    print(lines)

if __name__ == '__main__':
    main()
