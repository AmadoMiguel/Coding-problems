# info format --> 'timestamp','count','type'
                #     Hour    nPeople  In/Out

def busiestTime(info):
    startBusiestTime = 0
    endBusiestTime = 0
    nPeople = 0
    nMaxPeople = 0
    maxPeopleBuild = False
    # Iterate over the information
    for r in info:
        # Count in the number of people if they got into the bulding
        if r['type'] == 'enter':
            nPeople += r['count']
        # Decrease in case people got out    
        elif r['type'] == 'exit':
            nPeople -= r['count'] 
        # Register the end of busiest time in building
        if maxPeopleBuild:
            if nPeople < nMaxPeople:
                endBusiestTime = r['timestamp']  
                maxPeopleBuild = False  
        # Update max number of people inside and the time
        if nPeople > nMaxPeople:
            # Register the start of busiest time in building
            startBusiestTime = r['timestamp']
            nMaxPeople = nPeople   
            maxPeopleBuild = True       

    return (startBusiestTime,endBusiestTime)        

buildInfo = [
    {'timestamp': 1546711314, 'count': 10, 'type': 'enter'}, 
    {'timestamp': 1546711379, 'count': 13, 'type': 'enter'}, 
    {'timestamp': 1546711496, 'count': 2, 'type': 'exit'}, 
    {'timestamp': 1546711578, 'count': 1, 'type': 'exit'}, 
    {'timestamp': 1546711673, 'count': 1, 'type': 'enter'}, 
    {'timestamp': 1546711755, 'count': 1, 'type': 'enter'}, 
    {'timestamp': 1546711764, 'count': 5, 'type': 'exit'}, 
    {'timestamp': 1546711778, 'count': 3, 'type': 'exit'}, 
    {'timestamp': 1546711799, 'count': 3, 'type': 'enter'}, 
    {'timestamp': 1546711851, 'count': 5, 'type': 'exit'}
]    

print( busiestTime(buildInfo) )