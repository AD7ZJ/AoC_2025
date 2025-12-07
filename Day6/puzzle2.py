import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    
    matrix = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            #line = line.strip()
            matrix.append(list(line))
    print(matrix)


    # the operator is always left aligned to the number column
    accum = 0

    # find the next operator
    matrix[-1]

    columnAcc = 0
    columnStart = 0
    nextColumnStart = 0
    x = 0
    while x < len(matrix[0]):
        if x == nextColumnStart:
            columnStart = nextColumnStart
            accum += columnAcc
            columnAcc = 0

            # find where the next column starts by looking for the * or + operator
            for i in range(x, x+8):
                if matrix[-1][i] == "*" or matrix[-1][i] == "+":
                    nextColumnStart = i
                    break
            
            op = matrix[-1][columnStart]
            print("")
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
        #print(f" Total: {columnAcc}")

        

    print(f"Total: {accum}")


if __name__ == "__main__":
    main()