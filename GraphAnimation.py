import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import datetime

import ComRead
import threading

now = datetime.datetime.now()
title = "T-motor_mn-5212-8-kv-340_2x18inch_XrotorPro50A"
fileName = str("%s_%.4d-%.2d-%.2dT%.2d-%.2d-%.2d.txt"%(title, now.year, now.month, now.day, now.hour, now.minute, now.second))
thread = threading.Thread(target=ComRead.ReadArduinoData, args=(fileName,))
thread.daemon = True
thread.start()

# style.use('fivethirtyeight')

fig = plt.figure()
plt.title(title)
plt.xlabel("time")
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

def animate(i):
    graph_data = open(fileName,'r').read()
    lines = graph_data.split('\n')
    time = []
    weight = []
    amps = []
    accVolts = []
    effs = []
    temps = []
    for line in lines:
        if len(line) > 1:
            l = line.split('\t')
            time.append(float(l[0]))
            weight.append(float(l[1]))
            amps.append(float(l[2]))
            effs.append(float(l[7]))
            accVolts.append(float(l[3]))
    ax1.clear()
    ax1.plot(time, weight)
    ax2.plot(time, amps)
    ax3.plot(time, effs)
    ax4.plot(time, accVolts)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
