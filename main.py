motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
minDist = int(input())
maxDist = int(input())
n = int(input())
for i in range(n):
    motels.append(int(input()))
motels.sort()
cache = {}


def getAllPaths(startIdx: int, endIdx: int) -> int:
    if startIdx == endIdx:
        return 1
    if startIdx == endIdx - 1:
        distance = motels[endIdx] - motels[startIdx]
        if minDist <= distance <= maxDist:
            return 1
        else:
            return 0

    if (startIdx, endIdx) in cache:
        return cache[(startIdx, endIdx)]

    possibleStops = []
    for i in range(startIdx + 1, endIdx+1, 1):
        distance = motels[i] - motels[startIdx]
        if distance > maxDist:
            break
        if distance >= minDist:
            possibleStops.append(i)
    sum = 0
    for stopIdx in possibleStops:
        sum += getAllPaths(stopIdx, endIdx)
    cache[(startIdx, endIdx)] = sum
    return sum


print(getAllPaths(0, len(motels) - 1))
