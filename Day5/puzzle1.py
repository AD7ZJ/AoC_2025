import sys

def CheckIfNInRange(ranges, n):
    lo = 0
    hi = len(ranges) - 1
    check = 0
    while lo <= hi:
        check = (lo + hi) // 2

        if ranges[check][0] <= n <= ranges[check][1]:
            return True
        elif n < ranges[check][0]:
            hi = check - 1
            #print(f"{n} is < {ranges[check]}. hi: {hi} lo: {lo}")
        else:
            lo = check + 1
            #print(f"{n} is > {ranges[check]}. hi: {hi} lo: {lo}")

    return False

        
    

def CombineAndSortRanges(ranges):
    ranges = sorted(ranges)
    combined = []
    for start, end in ranges:
        if not combined or start > combined[-1][1]:
            # -1 means the last index of the list. So if start is greater than the end of the last entry, add this tuple. 
            combined.append([start, end])
        else:
            # update the end of this tuple to the new larger value
            combined[-1][1] = max(combined[-1][1], end)
    return combined


def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    
    freshRanges = []
    rangesRead = False
    accum = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                # a blank line means we're done reading ranges
                rangesRead = True
                freshRanges = CombineAndSortRanges(freshRanges)
                print(freshRanges)
                continue

            if not rangesRead:
                start, end = line.split("-")
                freshRanges.append((int(start), int(end)))
            else:
                if CheckIfNInRange(freshRanges, int(line)):
                    accum += 1
                    print(f"{line} was fresh!")
                else:
                    print(f"{line} was NOT fresh!")
    
    print(f"There are {accum} fresh ingredients!")


if __name__ == "__main__":
    main()