# # 1 . DATETIME.DATETIME

# from datetime import datetime, date, time

# # METHODES
# # NOW()

# now = datetime.now()
# print(now)

# # TODAY

# today = datetime.today()
# print(today)

# # COMBINE 

# my_date = date(2025,12,25)
# my_time = time(10,30,00)
# combine = datetime.combine(my_date, my_time)
# print(combine)

# # STRFTIME

# n = datetime.now()
# strftime = n.strftime("%Y-%M-%D    %H:%M:%S")
# print(strftime)

# # STRPTIME

# dtsrt = "14/09/2024 15:45:30"
# strptime = datetime.strptime(dtsrt, "%d, %m, %Y    %H:%M:%S")
# print(strptime)

# # 2 . DATETIME DATE

# from datetime import date
# import time
# # METHODE
# # TODAY

# today = date.today()
# print(today)

# # FROMTIMESPAMP

# ts = time.time()
# fts = date.fromtimestamp(ts)
# print(fts)

# # ISOFORMAT

# td = date.today()
# iso = td.isoformat()
# print(iso)

# 3. DATETIME TIME

from datetime import time, datetime

t = time(13, 30, 50)
print(t)

# METHODE
# HOUR

dt = datetime.now()

h = dt.hour
print(h)

# MINUTE

m = dt.minute
print(m)

# SECOND

s = dt.second
print(s)

# MICROSECOND

ms = dt.microsecond
print(ms)