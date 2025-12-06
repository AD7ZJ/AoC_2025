import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    
    matrix = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            matrix.append(line.split())

    accum = 0
    for x in range(len(matrix[0])):
        columnAcc = 0
        op = matrix[-1][x] # operator is the last entry in the column
        if op == "*":
            columnAcc = 1
        for y in range(len(matrix) - 1):
            if op == "+":
                columnAcc += int(matrix[y][x])
            elif op == "*":
                columnAcc = columnAcc * int(matrix[y][x])

        accum += columnAcc

    print(f"Total: {accum}")


if __name__ == "__main__":
    main()