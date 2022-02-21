hour, minute = input().split()
time = int(input(""))

hour = int(hour)
minute = int(minute)

minute = hour * 60 + minute
minute = minute + time

hour = minute // 60 
minute = minute % 60

if hour > 23:
    hour -= 24

print(hour, minute)