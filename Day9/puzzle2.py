import math
import sys

import matplotlib.pyplot as plt


def main():
    if len(sys.argv) < 2:
        print("Usage: python puzzle2.py <filename>")
        return
    
    pointList = []
    xList = []
    yList = []

    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            x,y = line.split(',')
            pointList.append((int(x),int(y)))
            xList.append(int(x))
            yList.append(int(y))


    # stop = 50
    # plt.scatter(xList[:stop], yList[:stop], s=10)
    # plt.gca().invert_yaxis() 
    # plt.show()

    # compress all of these widely spaced points into a more compact grid

    # get sorted unique coordinates
    all_x = sorted({p[0] for p in pointList})  # unique Xs, sorted ascending
    all_y = sorted({p[1] for p in pointList})  # unique Ys, sorted ascending

    # build compression maps
    xCompressMap = {x: i for i, x in enumerate(all_x)}
    yCompressMap = {y: i for i, y in enumerate(all_y)}

    # build decompression maps
    xDeCompressMap = {i: x for i, x in enumerate(all_x)}
    yDeCompressMap = {i: y for i, y in enumerate(all_y)}

    # build compressed point list
    compressedPointList = [(xCompressMap[x], yCompressMap[y]) for x, y in pointList]

    # Initialize all cells as empty ('.')
    grid = []
    for y in range(len(pointList)):
        row = []
        for x in range(len(pointList)):
            row.append('.')  # empty cell
        grid.append(row)

    # mark the red tiles
    for point in pointList:
        x = point[0]
        y = point[1]

        # convert real coordinates to compressed indices
        xi = xCompressMap[x]
        yi = yCompressMap[y]
        grid[yi][xi] = '#'

    # go from point to point now, marking green tiles in the compressed grid. We can assume all points are in order, and either move
    # horizontally or vertically, not both at the same time. 
    for i in range(len(pointList)):
        x1, y1 = pointList[i]
        x2, y2 = pointList[(i+1) % len(pointList)]
        xi1, yi1 = xCompressMap[x1], yCompressMap[y1]
        xi2, yi2 = xCompressMap[x2], yCompressMap[y2]

        if xi1 == xi2:
            # vertical movement
            for yi in range(min(yi1, yi2), max(yi1, yi2)+1):
                if grid[yi][xi1] == '.':
                    grid[yi][xi1] = 'X'
        elif yi1 == yi2:
            # horizontal movement
            for xi in range(min(xi1, xi2), max(xi1, xi2)+1):
                if grid[yi1][xi] == '.':
                    grid[yi1][xi] = 'X'


    # now we try to mark all the points outside, and what's left will be inside...
    height = len(yCompressMap)
    width = len(xCompressMap)

    outsideVisited = [[False]*width for _ in range(height)]
    # start from top-left corner
    stack = [(0, 0)]

    while stack:
        xi, yi = stack.pop()
        if xi < 0 or xi >= width or yi < 0 or yi >= height: 
            continue
        if outsideVisited[yi][xi] or grid[yi][xi] != '.':
            continue
        outsideVisited[yi][xi] = True
        # try to spread out one step in all directions
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            stack.append((xi+dx, yi+dy))

    # Any '.' not visited is interior
    for yi in range(height):
        for xi in range(width):
            if grid[yi][xi] == '.' and not outsideVisited[yi][xi]:
                grid[yi][xi] = 'X' # mark it green


    # for y in range(len(pointList)):
    #     for x in range(len(pointList)):
    #         print(f"{grid[y][x]}", end="")
    #     print("\n")


    rectList = CalcAllRectangleAreasBf(pointList)

    # sort based on the area (element 0 of the tuple)
    rectList.sort(key=lambda tup: tup[0], reverse=True)

    for rect in rectList[:10]:
        area, p1, p2 = rect
        doesIt = DoesRectangleContainOnlyRedOrGreen(grid, xCompressMap[p1[0]], yCompressMap[p1[1]], xCompressMap[p2[0]], yCompressMap[p2[1]])
        print(f"{rect} {doesIt}")

    # for rect in rectList[:10]:
    #     areaComp, pi1, pi2 = rect
    #     x1 = xDeCompressMap[pi1[0]]
    #     y1 = yDeCompressMap[pi1[1]]
    #     x2 = xDeCompressMap[pi2[0]]
    #     y2 = yDeCompressMap[pi2[1]]
    #     realArea = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    #     print(f"{realArea} ({x1},{y1}) ({x2}, {y2})")

    

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


def DoesRectangleContainOnlyRedOrGreen(grid, xi1, yi1, xi2, yi2):
    min_xi = min(xi1, xi2)
    max_xi = max(xi1, xi2)
    min_yi = min(yi1, yi2)
    max_yi = max(yi1, yi2)

    for yi in range(min_yi, max_yi + 1):
        for xi in range(min_xi, max_xi + 1):
            cell = grid[yi][xi]
            if cell != '#' and cell != 'X':
                return False
    return True


if __name__ == "__main__":
    main()
