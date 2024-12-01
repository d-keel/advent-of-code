def readFile(filePath: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    with open(filePath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            splitLine: list[str] = line.split(sep='   ')
            left.append(int(splitLine[0]))
            right.append(int(splitLine[1])) 
    
    return left, right

def sortValues(left: list[int], right: list[int]) -> tuple[list[int], list[int]]:
    return sorted(left), sorted(right)

def calculateDifference(left: list[int], right: list[int]) -> int:
    total: int = 0

    for i, v in enumerate(left):
        total += abs(v - right[i])

    return total

def main() -> None:
    left, right = readFile('input.txt')
    left, right = sortValues(left, right)
    total: int = calculateDifference(left, right)
    print(total)


if __name__ == "__main__":
    main()
