
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    

    with open(sys.argv[1], "r") as f:
        accum = 0
        for line in f:
            line = line.strip()
            jolts = 0
            for i in range(len(line) - 1):
                scoreTens = 10 * int(line[i])

                for j in range(i+1, len(line)):
                    scoreOnes = 1 * int(line[j])
                    #print(f"{scoreTens} + {scoreOnes}")

                    if scoreTens + scoreOnes > jolts:
                        jolts = scoreTens + scoreOnes

            print(line, jolts)
            accum += jolts
        print("total: ", accum)
 

if __name__ == "__main__":
    main()