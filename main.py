import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from numpy import loadtxt
import glob
#import pylab as p
import time
import os
from pathlib import Path

folder_path_str = input('Enter /path/to/data folder/):')
folder_path = Path(folder_path_str)

most_recent_file = None
most_recent_time = 0

while True:
    # iterate over the files in the directory using os.scandir
    # 
    for entry in os.scandir(folder_path):
        if entry.is_file():
            # get the modification time of the file using entry.stat().st_mtime_ns
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                # update the most recent file and its modification time
                most_recent_file = entry.name
                most_recent_time = mod_time

    data_set = np.loadtxt(folder_path_str + most_recent_file, delimiter=',')
    N = len(data_set)                                 
    
    spectrum = np.zeros(N)
    freq = np.ones(N)
    freq = data_set[:,0]
    spectrum = data_set[:,1]

    average_signal = np.average(spectrum)
    area = N*average_signal

    #Graph

    font1 = {'family': 'serif',
            'color':  'darkblue',
            'weight': 'bold',
            'size': 18,
            }

    font2 = {'family': 'serif',
            'color':  'darkred',
            'weight': 'bold',
            'size': 22,
            }

    font3 = {'family': 'serif',
            'color':  'black',
            'weight': 'bold',
            'size': 22,
            }

    graph_title = "Horn Spectrum"
    graph_subtitle = ""

    fig, ax = plt.subplots(1, figsize=(16, 12))
    plt.title(graph_title, fontdict=font2)
    plt.suptitle(graph_subtitle, fontdict=font1)

    #plt.xlim([0,300])
    #plt.ylim([0,6000])
    plt.plot(freq, spectrum, label='', color='blue', linewidth=2)

    plt.xlabel("Frequency (MHz)", fontdict=font3)
    plt.ylabel("Signal", fontdict=font3)

    #Set tick marks
    # ax.xaxis.set_major_locator(MultipleLocator(500))
    # ax.xaxis.set_minor_locator(MultipleLocator(100))

    # ax.yaxis.set_major_locator(MultipleLocator(200))
    # ax.yaxis.set_minor_locator(MultipleLocator(100))

    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)

    # Add grid lines
    plt.grid(visible=True, which='major', color='#666666', linestyle='-', linewidth=1)

    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    plt.savefig('/home/john/DSPIRA_2025/Spectrometers_browser/current_spectrum.png')
    #plt.show()
    plt.close()

    time.sleep(11.23)

    # Output to a file

    #output_array = np.zeros((time_number,2))
    #output_array[:,0] = time
    #output_array[:,1] = average_signal

    #textfilename = "Magnitude_Aug2_Lime.csv1"
    #np.savetxt(textfilename, output_array, delimiter=',')
