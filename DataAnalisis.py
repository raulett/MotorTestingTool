import tkinter

import matplotlib.pyplot as plt
import pylab
import pandas as pd

import scipy

from apm import *
from tkinter import *
from tkinter.filedialog import askopenfilename


filenames = tkinter.filedialog.askopenfilenames()
fig = pylab.figure()
ax1 = fig.add_subplot(211)
ax1.set_title(u'Efficiency graph')
ax2 = fig.add_subplot(212)

pylab.tight_layout(h_pad = -1.7)

ax1.yaxis.set_label_position('left')
ax1.set_ylabel('Efficiency, W/g')
ax2.yaxis.set_label_position('right')
ax2.set_ylabel('Amperage, A')
ax1.tick_params(axis='x', labelbottom='off', labeltop='off')
ax2.tick_params(axis='y', labelleft='off', labelright='on', left=False, right=True)
for ax in fig.axes:
    ax.grid(True)

for filename in filenames:
    file = open(filename, 'r')
    dataframe = pd.read_csv(file, sep='\t')
    title = os.path.basename(file.name).split('_')[0:4]
    dataframe = dataframe[dataframe['Weight, g'] >= 500]
    dataframe = dataframe[dataframe['Efficiency g/w'] >= 0]
    dataframe = dataframe[dataframe['Efficiency g/w'] <= 20]
    dataframe = dataframe.sort_values(by=['Weight, g'])
    dataframe['AmperageEff'] = dataframe['Weight, g']/dataframe['Amperage, A']
    polynomWE = scipy.polyfit(dataframe['Weight, g'], dataframe['Efficiency g/w'], 3)
    polynowWA = scipy.polyfit(dataframe['Weight, g'], dataframe['Amperage, A'], 3)
    ax1.plot(dataframe['Weight, g'], scipy.polyval(polynomWE, dataframe['Weight, g']), label = title)
    ax2.plot(dataframe['Weight, g'], scipy.polyval(polynowWA, dataframe['Weight, g']), label = title)


ax1.legend(loc='upper right')
ax2.legend(loc='upper left')
pylab.show()
