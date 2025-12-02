

import sys

accum = 0
patternsSeen = set()

def FindRangeOfSplitableNumbers(start: str, end: str) -> tuple[int, int]:
    # is there a number in this range that has a length evenly divisible by 2?
    startLen = len(start)
    endLen = len(end)
    
    if (startLen % 2 == 0):
        # the start is already evenly divisible, so we start there
        startsAt = int(start)
    else:
        # we would have to start at the next power of 10
        startsAt = 10 ** (startLen)

    if (endLen % 2 == 0):
        # the end is already evenly divisible, so we stop there
        endsAt = int(end)
    else:
        # we would have to stop at the previous power of 10 minus 1
        endsAt = (10 ** (endLen - 1)) - 1
    
    if startsAt < endsAt:
        return startsAt, endsAt
    else:
        # there are no splittable numbers
        return 0, 0


# splits number in half. Assumes it's evenly divisible
def SplitNumber(num: int) -> list[str]:
    numStr = str(num)
    middle = len(numStr) // 2
    return [numStr[:middle], numStr[middle:]]

def CheckForPatterns(start: int, end: int) -> list[int]:
    global accum
    global patternsSeen
    patternList = []

    print(f"{start}-{end}   ", end="")

    num = SplitNumber(start)

    searchStart = int(num[0])

    #the smallest possible pattern will be the first half repeated. But even that might be too large...
    pattern = int(str(searchStart) + str(searchStart))

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

    print(f"\n\nTotal: {accum}")   
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
            startSearch, endSearch = FindRangeOfSplitableNumbers(start, end)
            if startSearch != 0:
                CheckForPatterns(startSearch, endSearch)

        #print(ranges)

if __name__ == "__main__":
    main()