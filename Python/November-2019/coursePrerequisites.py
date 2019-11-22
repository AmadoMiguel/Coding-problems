# You are given a hash table where the key is a course code, and the value is a list of all the course codes
# that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such
# ordering exists, return NULL.
#
# Example:
# {
#   'CSC300': ['CSC100', 'CSC200'],
#   'CSC200': ['CSC100'],
#   'CSC100': []
# }
#
# This input should return the order that we need to take these courses:
#  ['CSC100', 'CSC200', 'CSCS300']


def getCoursesOrdering(coursesMap):
    return orderCourses([], coursesMap)


# Basically as prerequisites are met, remove the course from the map
def orderCourses(coursesToTake, coursesMap):
    nextCourse = None
    if len((list(coursesMap.keys()))) > 0 and coursesToTake is not None:
        if coursesToTake in coursesMap.values():
            for course in coursesMap.keys():
                if coursesMap[course] == coursesToTake:
                    nextCourse = course
            if nextCourse is not None:
                coursesToTake.append(nextCourse)
                del coursesMap[nextCourse]
                coursesToTake = orderCourses(coursesToTake, coursesMap)
            else:
                coursesToTake = None
        else:
            coursesToTake = None

    return coursesToTake


print(getCoursesOrdering({
                          'CSC300': ['CSC100', 'CSC200'],
                          'CSC200': ['CSC100'],
                          'CSC100': [],
                          'CSC400': ['CSC100', 'CSC200', 'CSC300']
                        }))
