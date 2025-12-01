#!/bin/python3
# pyright: reportAny = false, reportExplicitAny = false

from typing import Any, override

class Node:
    def __init__(self, data: Any):
        self.data: int = data
        self.next: Node | None = None
        self.prev: Node | None = None

"""

END CLASS NODE

"""

class CircularDoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, data: Any):
        newNode: Node = Node(data)

        if not self.head:
            newNode.next = newNode.prev = newNode
            self.head = newNode

        else:
            last: Node | None = self.head.prev

            newNode.next = self.head
            newNode.prev = last
            self.head.prev = newNode
            last.next = newNode                                                 # pyright: ignore[reportOptionalMemberAccess]

            self.head = newNode
            
    def walk(self):
        if not self.head:
            print("Empty")
            return

        current: Node = self.head

        while True:
            print(current.data, end=' <-> ')
            current = current.next                                              # pyright: ignore[reportAssignmentType]
            if current == self.head:
                break
        print()

"""

END CLASS CIRCULARDOUBLYLINKEDLIST

"""

class RotationLock(CircularDoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.choice: Node | None = self.head
        self.size: int = 0

    @override
    def append(self, data: Any):
        super().append(data)
        self.choice = self.head
        self.size += 1

    def rotate(self, turnLeft : bool, count: int) -> int:
        zeroes: int = 0
        if not self.head:
            print("Empty")
            return zeroes

        if turnLeft:
            for _ in range(count):
                #Turning Left
                self.choice = self.choice.prev                                  # pyright: ignore[reportOptionalMemberAccess]
                if self.choice.data == 0:
                    zeroes += 1
        else:
            for _ in range(count):
                #Turning Right
                self.choice = self.choice.next                                  # pyright: ignore[reportOptionalMemberAccess]
                if self.choice.data == 0:
                    zeroes += 1
        return zeroes

    def rotateToValue(self, value: int):
        if not self.choice:
            print("Empty")
            return

        curVal: int = int(self.choice.data)

        while curVal != value:
            _ = self.rotate(True, 1)
            curVal = int(self.choice.data)

"""

END CLASS ROTATIONLOCK

"""

def readFile(filePath: str) -> list[str]:
    lines: list[str] = []

    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    return lines

def main():
    lines: list[str] = readFile('sample.txt')
    count: int = 0
    zeroes: int = 0
    rLock: RotationLock = RotationLock()

    for i in range(0,100):
       rLock.append(i)

    #rLock.walk()
    rLock.rotateToValue(50)

    for line in lines:
        turnLeft: bool = False
        if line[0] == 'L':
            turnLeft = True
        elif line[0] == 'R':
            turnLeft = False

        zeroes += rLock.rotate(turnLeft, int(line[1:]))
        
        if rLock.choice.data == 0:                                              # pyright: ignore[reportOptionalMemberAccess]
            count += 1

    print("Part 1 Count: ", count)
    print("Part 2 Count: ", zeroes)


if __name__ == '__main__':
    main()
