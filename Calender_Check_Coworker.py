from datetime import datetime

# importing datetime package will help in conversion of time format

# input parameters

YourCalendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
YourWorkingHours = ['9:00', '20:00']

YourCoWorkersCalendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
YourCoWorkersWorkingHours = ['10:00', '18:30']

meetingDuration = 30


def appointments(calendar):
    # this function will help to convert the given input list datatype to string and store in the allAppointmrnts list
    allAppointments = []

    for appointment in calendar:
        appointmentStart = appointment[0]
        appointmentEnd = appointment[1]

        allAppointments.append({
            'start': datetime.strptime(appointmentStart, '%H:%M'),
            'end': datetime.strptime(appointmentEnd, '%H:%M')
        })

    return allAppointments


def free_times(workingHours, appointments):
    # this function will help to compare the working and meeting hours and will output the available free time of individual workers

    all_free_time = []

    for i, value in enumerate(appointments):
        if i == 0:
            if value['start'] != workingHours['start']:
                all_free_time.append([
                    workingHours['start'],
                    value['start']
                ])
            if value['end'] != appointments[i + 1]['start']:
                all_free_time.append([
                    value['end'],
                    appointments[i + 1]['start']
                ])
        elif 0 < i < (len(appointments) - 1):
            if value['end'] != appointments[i + 1]['start']:
                all_free_time.append([
                    value['end'],
                    appointments[i + 1]['start']
                ])
        elif i == (len(appointments) - 1):
            if value['end'] != workingHours['end']:
                all_free_time.append([
                    value['end'],
                    workingHours['end']
                ])

    return all_free_time


def meeting_possibilities(myFreeTime, myColleaguesFreeTime):
    # this function will help to output the time available between the two worker
    meeting_possibilities_list = []
    # checking the start and end time between the two worker to get the free meeting slots
    for mySlots in myFreeTime:
        for colleaguesSlot in myColleaguesFreeTime:
            if mySlots[1] > colleaguesSlot[0] and mySlots[0] < colleaguesSlot[1]:

                if mySlots[0] > colleaguesSlot[0]:
                    startTime = mySlots[0].strftime('%H:%M')
                else:
                    startTime = colleaguesSlot[0].strftime('%H:%M')

                if mySlots[1] < colleaguesSlot[1]:
                    endTime = mySlots[1].strftime('%H:%M')
                else:
                    endTime = colleaguesSlot[1].strftime('%H:%M')

                meeting_possibilities_list.append([startTime, endTime])

    return meeting_possibilities_list


# calling the appointment function to convert the YourCalendar input to string
myAppointments = appointments(YourCalendar)
myWorkingHours = {
    'start': datetime.strptime(YourWorkingHours[0], '%H:%M'),
    'end': datetime.strptime(YourWorkingHours[1], '%H:%M')
}
# calling to compare the working and meeting hours
myFreeTime = free_times(myWorkingHours, myAppointments)

# calling the appointment function to convert the YourCoWorkersCalendar input to string
colleaguesAppointments = appointments(YourCoWorkersCalendar)
colleaguesWorkingHours = {
    'start': datetime.strptime(YourCoWorkersWorkingHours[0], '%H:%M'),
    'end': datetime.strptime(YourCoWorkersWorkingHours[1], '%H:%M')
}
# calling to compare the co-worker working hour and meeting hours
myColleaguesFreeTime = free_times(colleaguesWorkingHours, colleaguesAppointments)

print(meeting_possibilities(myFreeTime, myColleaguesFreeTime))

# time and space complexity


# Time:
# The appointments() and free_times() functions have time complexity O(n), since they iterate over the list of appointments only once.
# But, meeting_possibilities() function uses nested loops to compare the free time slots of two calendars.
# The outer loop iterates over the free time slots of the first calendar, while the inner loop iterates over the free time slots
# of the second calendar. So, the time complexity will be O(n^2)


# Space:
# The space complexity depends on the size of the input passed and the output.
# So, the space complexity of input is O(n) and output is O(m) hence space complexity is O(n+m)
