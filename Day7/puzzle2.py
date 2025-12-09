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
    numPaths = SearchAllPossiblePaths(matrix[0].index('S'), 0, matrix)
    print(f"Found {numPaths} unique paths")


# I tried a regular depth first search algorithm, and that was taking waayyyy too long. We don't need the actual 
# paths, just the number of unique paths. 
def SearchAllPossiblePaths(startx, starty, matrix):
    height = len(matrix)
    width = len(matrix[0])

    # counts will track the number of times a column could be taken as a unique path
    counts = [0] * width
    counts[startx] = 1

    for y in range(starty, height - 1):
        next_counts = [0] * width
        for x in range(width):
            if counts[x] == 0:
                continue
            below_char = matrix[y + 1][x]
            if below_char == '.':
                # move straight down
                next_counts[x] += counts[x]
            elif below_char == '^':
                # split left and right, if in bounds
                if x - 1 >= 0:
                    next_counts[x - 1] += counts[x]
                if x + 1 < width:
                    next_counts[x + 1] += counts[x]

        # propagate the list to the next row
        counts = next_counts

    # unique paths = sum of counts in the bottom row
    return sum(counts)


def PrintMatrix(matrix):
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    main()