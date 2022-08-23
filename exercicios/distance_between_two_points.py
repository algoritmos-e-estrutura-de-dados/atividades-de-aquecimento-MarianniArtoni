from math import sqrt

x1 = round(float(input()),1)
y1 = round(float(input()),1)
x2 = round(float(input()),1)
y2 = round(float(input()),1)

print(f"{round((sqrt(((x2 - x1)**2) + ((y2 - y1)**2))),4)}")