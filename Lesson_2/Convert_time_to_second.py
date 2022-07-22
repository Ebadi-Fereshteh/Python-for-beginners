# Convert time to second
time = input()
x = time.split(':')

sec = float(x[0])*3600 + float(x[1])* 60 + float(x[2])

print(sec)


