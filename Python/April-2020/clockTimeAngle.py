# Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and
# the minute hands.
#
# Bonus: When, during the course of a day, will the angle be zero?

hoursAngles = {
    "00": 0, "01": 30, "02": 60, "03": 90, "04": 120, "05": 150, "06": 180,
    "07": 210, "08": 240, "09": 270, "10": 300, "11": 330, "12": 360
}

minutesAngles = {
    "00": 0, "05": 30, "10": 60, "15": 90, "20": 120, "25": 150, "30": 180,
    "35": 210, "40": 240, "45": 270, "50": 300, "55": 330, "60": 360
}


def findMinAngleForTime(time):
    hours, minutes = time.split(":")
    # Reject invalid time
    if hours > "24" or minutes > "60":
        print("Invalid time")
        return
    if len(hours) > 2 or len(minutes) > 2:
        print("Invalid time")
        return
    # Handle military time
    try:
        hourAngle = hoursAngles[hours]
    except KeyError:
        possibleAngle = str(int(hours) - 12)
        if len(possibleAngle) == 1:
            possibleAngle = "0" + possibleAngle
        hourAngle = hoursAngles[possibleAngle]
    try:
        minuteAngle = minutesAngles[minutes]
    except KeyError:
        prevKey, nextKey = None, None
        for k in minutesAngles.keys():
            if minutes > k:
                prevKey = k
                continue
            nextKey = k
            break
        minIndex = [m for m in range(int(prevKey), int(nextKey))].index(int(minutes))
        minuteAngle = [a for a in range(minutesAngles[prevKey], minutesAngles[nextKey] + 1, 5)][minIndex]
    dif = abs(hourAngle - minuteAngle)
    return min(dif, 360 - dif)


clockTime = "02:10"
print(findMinAngleForTime(clockTime))
