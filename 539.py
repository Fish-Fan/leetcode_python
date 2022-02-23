def findMinDifference(timePoints):
    minutes = list(map(calculateMinutes, timePoints))
    minutes.sort()
    return min((y - x) % 1440 for x, y in zip(minutes, minutes[1:] + minutes[:1]))

def calculateMinutes(time):
    return int(time[:2])*60 + int(time[3:])

if __name__ == '__main__':
    timePoints = ["12:01","00:10","00:01"]
    ans = findMinDifference(timePoints)
    print(ans)