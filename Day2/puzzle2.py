

import sys

accum = 0
patternsSeen = set()

def FindRangeOfSplitableNumbers(start: str, end: str, n: int) -> tuple[int, int]:
    # is there a number in this range that has a length evenly divisible by n?
    startLen = len(start)
    endLen = len(end)
    
    if (startLen % n == 0):
        # the start is already evenly divisible, so we start there
        startsAt = int(start)
    else:
        # we would have to start at the next power of 10
        startsAt = 10 ** (startLen - 1 + (n - (startLen % n))) 

    if (endLen % n == 0):
        # the end is already evenly divisible, so we stop there
        endsAt = int(end)
    else:
        # we would have to stop at the previous evenly dvisible power of 10 minus 1
        endsAt = (10 ** (endLen - (endLen % n))) - 1
    
    if startsAt < endsAt:
        return startsAt, endsAt
    else:
        # there are no splittable numbers
        return 0, 0


# splits number to give first n'th. Assumes it's evenly divisible by given n
def SplitNumber(num: int, n: int) -> int:
    numStr = str(num)
    split = len(numStr) // n
    return int(numStr[:split])

def CheckForPatternsOfLengthN(start: int, end: int, n: int) -> list[int]:
    global accum
    global patternsSeen
    patternList = []

    print(f"{start}-{end}   ", end="")

    searchStart = SplitNumber(start, n)

    #the smallest possible pattern will be this split repeated. But even that might be too large...
    pattern = int(str(searchStart) * n) # * on a string means concatenate n times

    while (pattern <= end):
        if pattern >= start:
            print(f" {pattern}, ", end="")

            if pattern not in patternsSeen:
                patternsSeen.add(pattern)
                patternList.append(pattern)
                accum += pattern
            else:
                print("We've seen this before: ", pattern)

        searchStart += 1
        pattern = int(str(searchStart) + str(searchStart))

    return patternList






def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    

    with open(sys.argv[1], "r") as f:
        line = f.readline().strip()
        ranges = line.split(',')

        for r in ranges:
            startAndEnd = r.split('-')
            start = startAndEnd[0]
            end = startAndEnd[1]

            for i in range(2, 6):
                startSearch, endSearch = FindRangeOfSplitableNumbers(start, end, i)
                if startSearch != 0:
                    CheckForPatternsOfLengthN(startSearch, endSearch, i)
                else:
                    print(f"\nNothing divisible by {i} for range {start}-{end} ")

            
            print(f"\n")   

        #print(ranges)

if __name__ == "__main__":
    main()