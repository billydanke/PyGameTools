
from datetime import datetime
from datetime import timedelta
import json

# Load every alarm file in the Alarms folder. Make a new alarm object for each one? I think so
# Then we can make an alarmDisplay class to show stuff from our alarms

# Time
# Days of the week to play on
# A name

alarmFilePath = 'Alarms/alarms.json'
alarmList = []
alarmDisplayList = []

def LoadAlarms():
    global alarmList
    with open(alarmFilePath,'r') as jsonFile:
        alarmDictList = json.load(jsonFile)
    for alarm in alarmDictList:
        alarmList.append(Alarm(alarm["hour"],alarm['minute'],alarm['isRepeatedDayDays']))
    
    alarmList = sorted(alarmList,key=TimeToAlarm)
    print("Alarms loaded:")
    for alarm in alarmList:
        print("Hour:",alarm.hour,"Minute:",alarm.minute)

def SaveAlarms():
    global alarmList
    with open(alarmFilePath,"w") as jsonFile:
        json.dump(alarmList,jsonFile,default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print("Alarms saved.")

def TimeToAlarm(alarm):
    now = datetime.now()
    alarmTime = datetime(alarm.year, alarm.month, alarm.day, alarm.hour, alarm.minute)
    timeDifference = alarmTime - now
    return timeDifference

class Alarm():
    def __init__(self, month, day, hour, minute, repeatedDays):
        self.year = datetime.now().year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.repeatedDays = repeatedDays
        self.muted = False

    def UpdateToNearestDay(self):
        current_day_of_week = datetime.now().weekday()

        nearest_day = None
        minTimeDifference = float('inf')

        for i, isRepeatedDay in enumerate(self.repeatedDays):
            if isRepeatedDay:
                dayDifference = (i - current_day_of_week) # will range from 6 to -6

                currentDateTime = datetime.now()
                hoursDifference = self.hour - currentDateTime.hour
                minutesDifference = self.minute - currentDateTime.minute
                nearestDateTime = currentDateTime + timedelta(days=dayDifference,hours=hoursDifference,minutes=minutesDifference)

                if(dayDifference < 0):
                    continue
                elif(dayDifference == 0 and nearestDateTime < currentDateTime):
                    print("closest day is before current time. Skipping.")
                    continue

                if dayDifference < minTimeDifference:
                    minTimeDifference = dayDifference
                    nearest_day = i

        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        nearest_day_name = day_names[nearest_day]

        print(f"The nearest alarm day is {nearest_day_name}, {nearestDateTime.month}-{nearestDateTime.day}-{nearestDateTime.year} @ {nearestDateTime.hour}:{nearestDateTime.minute}")
        return nearestDateTime
        
alarmList.append(Alarm(datetime.now().month,29,8,23,[False,False,False,True,False,False,False]))
alarmList.append(Alarm(datetime.now().month,26,9,23,[True,False,False,False,False,False,True]))

for alarm in alarmList:
    print(alarm.UpdateToNearestDay())
    #print(TimeToAlarm(alarm))

SaveAlarms()