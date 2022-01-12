import  time, os
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
workDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

print(days[2])

clearScreen(4)
# This will print all of the days
print(days)
clearScreen(4)
# This will print out all of the workdays
print(workDays)
clearScreen(4)
# This will print out all of the weekends
print(weekend)
clearScreen(4)
# This will print out all of the days in reverse
days.reverse()
print(days)
clearScreen(4)
# This will print out all of the workdays in reverse
workDays.reverse()
print(workDays)
clearScreen(4)
# This will print out all of the weekends in reverse workDays.reverse()
weekend.reverse()
print(weekend)
clearScreen(4)
