import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle2.py <filename>")
        return
    
    matrix = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            matrix.append(list(line))

    # the start is marked by 'S' on the first line
    numPaths = DepthFirstSearchAllPaths(matrix[0].index('S'), 0, matrix)
    print(f"Found {numPaths} unique paths")


def DepthFirstSearchAllPaths(startx, starty, matrix):
    height = len(matrix)
    width = len(matrix[0])

    # push the starting location onto the stack. The path at this point is a list of len 1...
    stack = [(startx, starty, [(startx, starty)])]

    completeUniquePaths = 0

    while stack:
        x, y, path = stack.pop()

        # if we've hit the last row, record this as a finished path
        if y == height - 1:
            completeUniquePaths += 1
            continue

        # look one row down
        ny = y + 1
        below_char = matrix[ny][x]

        if below_char == '.':
            # move straight down
            stack.append((x, ny, path + [(x, ny)]))
        elif below_char == '^':
            # split left and right, if in bounds
            if x - 1 >= 0:
                stack.append((x - 1, ny, path + [(x - 1, ny)]))
            if x + 1 < width:
                stack.append((x + 1, ny, path + [(x + 1, ny)]))

    # return number of unique paths
    return completeUniquePaths


def PrintMatrix(matrix):
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    main()