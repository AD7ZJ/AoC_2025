import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    
    matrix = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            matrix.append(list(line))

    accum = 0
    splittersHit = 0
    for y in range(1, len(matrix)):
        splitsSeen = set()
        for x in range(len(matrix[0])):
            charAbove = matrix[y-1][x]
            char = matrix[y][x]
            if charAbove == "S" and char != "^":
                matrix[y][x] = "|"
            if charAbove == "|" and char == ".": # propagate beam in free space
                matrix[y][x] = "|"
            if char == "^" and charAbove == "|": 
                splittersHit += 1
                # split the beam
                if matrix[y][x-1] == ".":
                    matrix[y][x-1] = "|"
                    splitsSeen.add(x-1)
                if matrix[y][x+1] == ".":
                    matrix[y][x+1] = "|"
                    splitsSeen.add(x+1)

        accum += len(splitsSeen)
        PrintMatrix(matrix)
        print(f"Saw {len(splitsSeen)} splits\n")

    print(f"Total: {accum} splits, {splittersHit} splitters hit")


def PrintMatrix(matrix):
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    main()