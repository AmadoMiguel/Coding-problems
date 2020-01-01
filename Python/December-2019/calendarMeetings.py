# Given 2 people agendas, their overall availability (time bounds) and a minimum meeting time gap, find all possible
# time intervals for which they could setup a meeting


def parseTime(time):
    indexOfColon = list(time).index(':')
    return int(time[0:indexOfColon]), int(time[indexOfColon + 1:])


def getTimeInterval(time1, time2):
    return [time1[1], time2[0]]


def compareTimes(time1, time2):
    # 0 -> equal
    # 1 -> time1 ahead of time2
    # -1 -> time2 ahead of time1
    hours1, mins1 = parseTime(time1)
    hours2, mins2 = parseTime(time2)
    if hours1 > hours2:
        return 1
    if hours1 < hours2:
        return -1
    if hours1 == hours2:
        if mins1 > mins2:
            return 1
        if mins1 < mins2:
            return -1
        if mins1 == mins2:
            return 0


def getTime(hrs, mins):
    if mins < 10:
        minsStr = "0" + str(mins)
    else:
        minsStr = str(mins)
    return str(hrs) + ":" + minsStr


def getMinutes(start, end):
    hours1, mins1 = parseTime(start)
    # Minutes counter
    totalMinutes = 0
    while compareTimes(getTime(hours1, mins1), end) == -1:
        if mins1 == 60:
            mins1 = 0
            hours1 += 1
        mins1 += 1
        totalMinutes += 1
    return totalMinutes


def getAvailableTimeSlots(calendar, schedule):
    availablePerson = []
    for i in range(len(calendar)):
        # Get last time for this interval
        lastTime = calendar[i]
        if i < len(calendar) - 1:
            nextTime = calendar[i + 1]
            if compareTimes(lastTime[1], nextTime[0]) == -1:
                availablePerson += [getTimeInterval(lastTime, nextTime)]
        else:
            # Handle case where times interval is last one in calendar
            if compareTimes(lastTime[1], schedule[1]) == -1:
                availablePerson += [[lastTime[1], schedule[1]]]
    return availablePerson


def findAvailableInterval(time1, time2):
    # Check start times
    avStartTime, avEndTime = None, None
    if compareTimes(time1[0], time2[0]) >= 0:
        avStartTime = time1[0]
    elif compareTimes(time1[0], time2[0]) == -1:
        avStartTime = time2[0]
    # Check end times
    if compareTimes(time1[1], time2[1]) <= 0:
        avEndTime = time1[1]
    elif compareTimes(time1[1], time2[1]) == 1:
        avEndTime = time2[1]
    return avStartTime, avEndTime


# Brute-force approach for now
def checkAvailabilities(cal1, sch1, cal2, sch2, minRange):
    globalAvailableBlocks = []

    # Get both people available time slots
    # O(N+M)
    availablePerson1 = getAvailableTimeSlots(cal1, sch1)
    availablePerson2 = getAvailableTimeSlots(cal2, sch2)

    # O(len(availablePerson1) * len(availablePerson2))
    for av1 in availablePerson1:
        for av2 in availablePerson2:
            avStartTime, avEndTime = findAvailableInterval(av1, av2)
            if avStartTime is not None and avEndTime is not None:
                # Obviously start time has to be before end time
                if compareTimes(avStartTime, avEndTime) == -1:
                    # At least should fit in the meeting range
                    if getMinutes(avStartTime, avEndTime) >= minRange:
                        globalAvailableBlocks += [[avStartTime, avEndTime]]

    print("Available intervals for person 1", availablePerson1)
    print("Available intervals for person 2", availablePerson2)

    return globalAvailableBlocks


meetingRange = 20

person1 = [['9:00', '9:30'], ['10:05', '10:22'], ['10:40', '11:25'], ['12:00', '13:00'], ['16:00', '18:00']]
person1Schedule = ['9:00', '20:00']

person2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
person2Schedule = ['10:00', '18:30']

print("Possible meeting times:", checkAvailabilities(person1, person1Schedule, person2, person2Schedule, meetingRange))
