orderedCourses = []
allCourses = {'CSC400':['CSC100','CSC300','CSC200'],'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}

def sortCourses():
    global allCourses
    global orderedCourses
    for k,v in allCourses.items():
        # If no prerequisites
        if not len(v):
            orderedCourses.append(k)
            # Remove course with prereq from hashmap
            del allCourses[k]  
            # Call recursively
            sortCourses()    
        # If more than one prerequisite    
        elif len(v) > 1:
            for p in v :
                if p not in orderedCourses:
                    orderedCourses.append(p)       
        # If just one prerequisite            
        else:
            if v[0] not in orderedCourses:
                orderedCourses.append(v[0]) 
        # Add final class in pensum
        if k not in orderedCourses:
            orderedCourses.append(k)                          


sortCourses()    
print(orderedCourses)    