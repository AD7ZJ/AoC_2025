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
            x,y,z = line.split(',')
            pointList.append((int(x),int(y),int(z)))

    # returns a tuple like this: (316.90219311326956, (162, 817, 812), (425, 690, 689))
    distanceCache = CalcDistBetweenAllPairsBf(pointList)

    # sort based on the distance (element 0 of the tuple)
    distanceCache.sort(key=lambda tup: tup[0])

    circuitList = []
    connectionsMade = 0
    totalConnectionsToMake = 1000 
    for entry in distanceCache:
        if connectionsMade >= totalConnectionsToMake:
            break

        p1 = entry[1]
        p2 = entry[2]

        g1 = FindCircuitGroup(circuitList, p1)
        g2 = FindCircuitGroup(circuitList, p2)

        if g1 == None and g2 == None:
            # start a new set
            circuitList.append({p1, p2})
            print(f"started a new group {p1} and {p2}")
            connectionsMade += 1
        elif g1 != None and g2 == None:
            g1.add(p2)
            print(f"added {p2}")
            connectionsMade += 1
        elif g1 == None and g2 != None:
            g2.add(p1)
            print(f"added {p1}")
            connectionsMade += 1
        elif g1 != g2:
            # merge these sets, this point pair is connecting them together
            g1.update(g2)
            circuitList.remove(g2)
            print(f"merged two sets")
            connectionsMade += 1
        elif g1 == g2:
            # do nothing but this still counts as a connection
            connectionsMade += 1
    

    # at this point we have a list of sets of the connected boxes. Sort so the largest are first....
    circuitList.sort(key=lambda s: len(s), reverse=True)

    for thing in circuitList:
        print(thing)

    puzzleAnswer = len(circuitList[0]) * len(circuitList[1]) * len(circuitList[2])
    print(f"The puzzle answer is {puzzleAnswer}")



def FindCircuitGroup(groups, point):
    for circuit in groups:
        if point in circuit:
            return circuit
    return None


def CalcDistBetweenAllPairsBf(list):
    distanceCache = []

    # brute force all possible pairs and cache the distance between them
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if i != j:
                p1 = list[i]
                p2 = list[j]
                dist = DistBetween2Points(p1, p2)
                distanceCache.append((dist, p1, p2))

    return distanceCache


def DistBetween2Points(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2 +
        (p1[2] - p2[2])**2
    )

if __name__ == "__main__":
    main()