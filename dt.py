# Importing datetime module

import datetime

## Print current time and date

print(datetime.datetime.now())

print("=" * 48)


## Print current year|month|day

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

print("=" * 48)


## Print current time|hour|minutes|seconds

print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)

print("=" * 48)


## Print a specific date : datetime.datetime(year, month, day [,hour, minute, second, millis])

print(datetime.datetime(1996,4,7,2))

print("=" * 48)

## Practice

birthDay = datetime.datetime(1996,7,4,2)
currentDate = datetime.datetime.now()

print(f"I lived for {currentDate - birthDay}")

# Date and time formatting

print(birthDay.strftime("%A"))
print(birthDay.strftime("%a"))
print(birthDay.strftime("%B"))
print(birthDay.strftime("%b"))
print(birthDay.strftime("%B %d, %Y"))