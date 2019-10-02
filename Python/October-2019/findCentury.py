# Given a year, find the century it belongs to


def findCentury(year):
    print(year)
    # Check if year is < 100
    if 0 < year <= 100:
        return 1
    else:
        # Divide number by 100
        cent = int(year / 100)
        # Check remainder
        rem = year % 100
        if rem > 0:
            cent += 1
        return cent


print(findCentury(2901))
