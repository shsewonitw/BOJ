import datetime as dt

hour , minute = map(int,input().split())

time = dt.datetime(year=dt.datetime.today().year, month=dt.datetime.today().month, day=dt.datetime.today().day, hour=hour, minute=minute)

prevTime = dt.timedelta(minutes=45)

resultTime = time - prevTime

print(int(resultTime.strftime('%H')), int(resultTime.strftime('%M')))


