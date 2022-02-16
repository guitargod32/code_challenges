import numpy

def findMinRooms(*args):
    #print(type(args))
    if hasErrors(args):
        return 0
    else:
        meetings = sorted(args, key=lambda i: (i[0], i[1])) #sort input by meeting start times
        numMeetings = len(args)
        activeMeetings = []
        for meet in range(numMeetings): #iterate through each meeting
            start = meetings[meet][0]
            end = meetings[meet][1]


            if (len(activeMeetings) == 0): #first meeting needs a room no matter what
                activeMeetings.append(meetings[meet])
            else:
                #endFirst = min(x[1] for x in activeMeetings)
                if start < activeMeetings[0][1]: #check if next meeting starts before or after the meeting that ends next ends (if before, add room)
                    
                    activeMeetings.append(meetings[meet])
                    activeMeetings = sorted(activeMeetings, key=lambda j: j[1]) #make sure meetings are sorted by end time
                else:
                    activeMeetings[0][1] = end #make ending of meeting that starts first now the ending of the new meeting
                    activeMeetings = sorted(activeMeetings, key=lambda j: j[1])
        return len(activeMeetings)
                

def hasErrors(inputs):
    meetingList = list(inputs)
    if not inputs:
        print("Error: Please enter meetings")
        return True
    
    for k in range(len(inputs)):
        if not isinstance(meetingList[k], list) or (len(meetingList[k]) <2):
            print("Error: Meetings must be formatted as lists using brackets")
            return True
        currentStart = meetingList[k][0]
        currentEnd = meetingList[k][1]
        
        if not (isinstance(currentStart, (int, float)) and (isinstance(currentEnd, (int, float)))):
            print("Error: Meeting times must all be of type float")
            return True
        if  (currentStart < 0.0) or (currentStart > 24.0) or (currentEnd < 0.0) or (currentEnd > 24.0):
            print("Error: Times must be between 0.0 and 24.0")
            return True
        if (currentStart > currentEnd):
            print("Error: Meeting start time must be earlier than end time")
            return True
        if  (len(meetingList[k]) != 2):
            print("Error: Please include exactly two times per meeting")
            return True
    return False
    