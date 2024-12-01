def readFile(filePath: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    with open(filePath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            splitLine: list[str] = line.split(sep='   ')
            leftNum, rightNum = int(splitLine[0]), int(splitLine[1])
            left.append(leftNum)
            right.append(rightNum)
    
    return left, right

def sortValues(left: list[int], right: list[int]) -> tuple[list[int], list[int]]:
    return sorted(left), sorted(right)

def calculateDifference(left: list[int], right: list[int]) -> tuple[int, int]:
    total: int = 0
    similarity: int = 0

    myDict: dict[int, int] = {}

    for i, v in enumerate(left):
        myDict[v] = myDict.get(v, 0)
        total += abs(v - right[i])

    for v in right:
        if v in myDict:
            myDict[v] += 1

    for k, v in myDict.items():
        score: int = k * v
        similarity += score

    return total, similarity

def main() -> None:
    left, right = readFile('input.txt')
    left, right = sortValues(left, right)
    total, similarity = calculateDifference(left, right)
    print(total, similarity)


if __name__ == "__main__":
    main()
