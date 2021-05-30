import serial
import time
import matplotlib.pyplot as plt
import numpy as np

port = "/dev/ttyACM0"
ser = serial.Serial(port, 9600)

times = []

for x in range(7):
    s = ser.readline().decode().rstrip()
    times.append(int(s))
    print(s)

times.pop(0)

times = [time - times[0] for time in times]
y = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

plt.plot(times, y, "bo")
plt.yticks(y)
plt.xticks(np.arange(min(times), max(times), 10))
plt.xlabel("Time, t (ms)")
plt.ylabel("Height, y, (m)")
plt.title("Height vs Time graph")
plt.savefig("plot.png")

gravity = (2 * 0.5) / (times[-1] / 1000)**2

print(times)
print(gravity)
