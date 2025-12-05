import sys

def CalcNumberOfAdjoining(matrix, x, y) -> int:
    numAdjoining = 0
    h, w = len(matrix), len(matrix[0])
    steps = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0),         (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    
    for dx, dy in steps:
        ax = x + dx
        ay = y + dy
        if 0 <= ax < w and 0 <= ay < h:
            if matrix[ay][ax] == "@":
                numAdjoining += 1

    return numAdjoining


def PrintMatrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            print(matrix[y][x], end="")
        print("")


def HarvestPaper(matrix):
    outputMatrix = []
    accum = 0
    for y in range(len(matrix)):
        row = ""
        for x in range(len(matrix[0])):
            if matrix[y][x] == '@':
                if CalcNumberOfAdjoining(matrix, x, y) < 4:
                    row += '.'
                    accum += 1
                else:
                    row += matrix[y][x]
            else:
                row += matrix[y][x]
        outputMatrix.append(list(row))
    
    return outputMatrix, accum

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle2.py <filename>")
        return
    
    matrix = []

    # read the whole file into a matrix
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            matrix.append(list(line))
    
    accum = 0
    paperCount = 1
    while paperCount != 0:
        matrix, paperCount = HarvestPaper(matrix)
        accum += paperCount
        #PrintMatrix(matrix)
        print(f"{paperCount} rolls of paper harvested this round. Total for all rounds: {accum}")


if __name__ == "__main__":
    main()