#!/bin/python3

def readFile(filePath: str) -> dict[int, list[list[int]]]:
    out: dict[int, list[list[int]]] = {}
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    for line in lines:
        gameNum = int(line.split(':')[0].split()[1])
        games = line.split(':')[1].split(';')
        for game in games:
            game = game.strip()
            perGame = game.split(',')
            #                       R G B
            colorList: list[int] = [0] * 3
            for color in perGame:
                num, c = int(color.split()[0]), color.split()[1]
                if c == 'red':
                    colorList[0] = num
                elif c == 'green':
                    colorList[1] = num
                elif c == 'blue':
                    colorList[2] = num
            if out.get(gameNum):
                out[gameNum].append(colorList)
            else:
                out[gameNum] = list([colorList])
    
    return out

def checkValid(gameData: list[list[int]]) -> bool:
    validGame: bool = True

    for lis in gameData:
        r, g, b = getRGB(lis)
        validGame = (r <= 12 and g <= 13 and b <= 14)
        if not validGame:
            return False

    return True

def getRGB(lis: list[int]) -> tuple[int, int, int]:
    return lis[0], lis[1], lis[2]

def getMaxCubes(gameData: list[list[int]]) -> int:
    #                   R G B
    needed: list[int] = [0] * 3

    for lis in gameData:
        r, g, b = getRGB(lis)
        needed[0] = max(needed[0], r)
        needed[1] = max(needed[1], g)
        needed[2] = max(needed[2], b)

    return needed[0] * needed[1] * needed[2]

def main() -> None:
    out = readFile('input.txt')
    validGames: list[int] = []
    neededPerGame: list[int] = []
    for k, v in out.items():
        if checkValid(v):
            validGames.append(k)
        neededPerGame.append(getMaxCubes(v))

    print(sum(validGames))
    print(sum(neededPerGame))


if __name__ == '__main__':
    main()
