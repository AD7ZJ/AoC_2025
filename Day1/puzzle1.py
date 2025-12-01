

import sys


safeDial = 50

# wrap safeDial between 0 - 100
def AddSafeDial(value: int):
    global safeDial
    safeDial = (safeDial + value) % 100

def main():
    global safeDial
    zeroCounter = 0

    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    

    with open(sys.argv[1], "r") as f:
        for line in f:
            leftOrRight = line[0]
            value = int(line[1:])
            if (leftOrRight == "L"):
                AddSafeDial(-value)
            else:
                AddSafeDial(value)

            print("The dial is rotated {} to point at {}".format(line.strip(), safeDial))
            if safeDial == 0:
                zeroCounter += 1
        
        print("The password is ", zeroCounter)

if __name__ == "__main__":
    main()