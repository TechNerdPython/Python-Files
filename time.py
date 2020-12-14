import datetime
import pytz

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_central = datetime_today.astimezone(pytz.timezone("US/Central"))
print(datetime_central)

# for tz in pytz.all_timezones:
#     print(tz)
