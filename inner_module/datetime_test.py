from datetime import datetime, timedelta, timezone

now = datetime.now()
dt = datetime(2015, 4, 19, 12, 20)
print(now)
print(dt)
print(type(now))
print(dt.timestamp())

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%a, %b %d %H:%M'))

now = now + timedelta(hours=10)
print(now)

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


