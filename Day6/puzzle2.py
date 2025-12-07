import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    
    matrix = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            matrix.append(list(line))

    accum = 0
    columnAcc = 0
    columnStart = 0
    nextColumnStart = 0
    x = 0
    while x < len(matrix[0]):
        if x == nextColumnStart:
            columnStart = nextColumnStart
            accum += columnAcc
            print(f"Col total: {columnAcc}")
            columnAcc = 0

            # find where the next column starts by looking for the * or + operator
            for i in range(x+1, x+8):
                if i < len(matrix[0]):
                    if matrix[-1][i] == "*" or matrix[-1][i] == "+":
                        nextColumnStart = i
                        print(f"Found the next colStart at {i}")
                        break
            
            op = matrix[-1][columnStart]
            if op == "*":
                columnAcc = 1
        
        colStr = ""
        for y in range(len(matrix) - 1):
            char = matrix[y][x]
            if char.isdigit():
                colStr += char
        
        if colStr.isdigit():
            if op == "+":
                columnAcc += int(colStr)
            elif op == "*":
                columnAcc = columnAcc * int(colStr)
                
        x += 1
        print(f"{colStr} {op} ", end="")

    # add the last column
    accum += columnAcc
    print(f"\nTotal: {accum}")


if __name__ == "__main__":
    main()