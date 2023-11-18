def meeting_room(meeting):
    meeting.sort(key=lambda x: (x[1], x[0]))
    count = 0
    endtime = 0
    for i in range(len(meeting)):
        if meeting[i][0] >= endtime:
            endtime = meeting[i][1]
            count += 1
    return count 
        

meeting = [[1, 4], [2, 3], [3, 5], [4, 6], [5, 7]]

meeting_room(meeting)
