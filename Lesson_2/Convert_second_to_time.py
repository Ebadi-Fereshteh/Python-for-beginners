# Convert second to time
second = float(input())

h = second/3600
m = (h - int(h)) * 60
s = (m - int(m)) * 60
if int(h) < 10:
    hour = ('0'+str(int(h)))
else:
    hour = int(h)
if int(m) < 10:
    min = ('0'+str(int(m)))
else:
    min = int(m)
if round(s) < 10:
    sec = ('0'+str(round(s)))
else:
    sec = round(s)

print(hour,':',min,':',sec)
# print(int(h))
# print(int(m))
# print(round(s))
# print(int(h),':',int(m),':',round(s))
