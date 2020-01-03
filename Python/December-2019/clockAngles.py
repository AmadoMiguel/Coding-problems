# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

clockAngles = {
    12: 0, 1: 30, 2: 60, 3: 90, 4: 120, 5: 150, 6: 180,
    7: 210, 8: 240, 9: 270, 10: 300, 11: 330
}

minutesMap = {}
minGap = 5
for j in range(1, 13):
    minutesMap[minGap] = j
    minGap += 5


def getAngleBetweenHourAndMinute(hours, minutes):
    gapBetweenHours = 30
    minuteAngle = clockAngles[minutesMap[minutes]]
    # For each 360* the minutes hand moves, the hours hand moves 30*
    hourAngle = clockAngles[hours] + int((minuteAngle * gapBetweenHours) / 360)
    return abs(hourAngle - minuteAngle)


print(getAngleBetweenHourAndMinute(12, 30))
