import math
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle1.py <filename>")
        return
    
    pointList = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            x,y = line.split(',')
            pointList.append((int(x),int(y)))

    rectList = CalcAllRectangleAreasBf(pointList)

    # sort based on the area (element 0 of the tuple)
    rectList.sort(key=lambda tup: tup[0], reverse=True)

    for rect in rectList[:10]:
        print(rect)


def CalcAllRectangleAreasBf(coordList):
    areaCache = []

    # brute force all possible rectangles and cache their area
    for i in range(len(coordList)):
        for j in range(i + 1, len(coordList)):
            if i != j:
                p1 = coordList[i]
                p2 = coordList[j]
                area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
                areaCache.append((area, p1, p2))

    return areaCache


if __name__ == "__main__":
    main()