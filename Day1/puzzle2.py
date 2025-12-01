

import sys


safeDial = 50

# wrap safeDial between 0 - 100
def AddSafeDialAndCountZerosBf(value: int) -> int:
    global safeDial
    zeroSpinCount = 0
    for i in range(abs(value)):
        if value < 0:
            safeDial -= 1
        else:
            safeDial += 1

        if safeDial < 0:
            safeDial = 99
        
        if safeDial >= 100:
            safeDial = 0

        if safeDial == 0:
            zeroSpinCount += 1

    if safeDial == 0 and zeroSpinCount > 0:
        zeroSpinCount -= 1 #don't double count if we end up on 0

    return zeroSpinCount


def AddSafeDialAndCountZeros(value: int) -> int:
    global safeDial
    quotient, remainder = divmod(safeDial + value, 100)
    safeDialStart = safeDial
    safeDial = remainder
    quotient = abs(quotient)
    if (quotient > 0 and (safeDial == 0 or safeDialStart == 0)):
        quotient -= 1 # don't double count if it ends or starts on 0
    return quotient

def main():
    global safeDial
    zeroCounter = 0

    if len(sys.argv) < 2:
        print("Usage: python puzzle2.py <filename>")
        return
    

    with open(sys.argv[1], "r") as f:
        for line in f:
            zerosDuringSpin = 0
            leftOrRight = line[0]
            value = int(line[1:])
            if (leftOrRight == "L"):
                zerosDuringSpin = AddSafeDialAndCountZerosBf(-value)
            else:
                zerosDuringSpin = AddSafeDialAndCountZerosBf(value)

            if zerosDuringSpin < 0:
                raise ValueError(f"Negative number detected: {zeroCounter}")
            
            print("The dial is rotated {} to point at {}. ".format(line.strip(), safeDial), end="")
            if (zerosDuringSpin > 0):
                print("During this turn it hit zero {} times".format(zerosDuringSpin))
            else:
                print(" ")
            zeroCounter += zerosDuringSpin
            if safeDial == 0:
                zeroCounter += 1
        
        print("The password is ", zeroCounter)

if __name__ == "__main__":
    main()