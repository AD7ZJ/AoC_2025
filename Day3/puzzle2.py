
import sys

def GetLargestWithinRange(startIdx: int, endIdx: int, line: str) -> tuple[str, int]:
    searchSpace = line[startIdx:endIdx]

    max = 0
    maxIdx = 0
    for i, ch in enumerate(searchSpace):
        if int(ch) > max:
            max = int(ch)
            maxIdx = i

    #print(f"  Searched {searchSpace} picked {max}")
    return str(max), maxIdx

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle2.py <filename>")
        return
    

    with open(sys.argv[1], "r") as f:
        accum = 0
        for line in f:
            line = line.strip()
            
            print(line, end="")

            # due to place value, we want the biggest numbers as far left as possible while still leaving enough remaining to the right to get 12 total
            start = 0
            end = len(line) - 11 # we have to leave enough possibilities to get the rest of the 12 numbers
            jolts = ""
            while len(jolts) < 12:
                largest, idx = GetLargestWithinRange(start, end, line)
                jolts += largest
                start += idx + 1
                end += 1 # each number we grab lets us search one closer to the end of the line next time around

            accum += int(jolts)
            print(f"{line}: {jolts}")

        print(f"Total: {accum}")

 

if __name__ == "__main__":
    main()