import sys
from IPython.display import display
from dataprocessing import loadData
import matplotlib.pyplot as plt
import numpy as np

how_to_use = "Usage: main.py [path to csv database]"

arguments = len(sys.argv)

if (arguments == 2 and (sys.argv[1] == 'h' or sys.argv[1] == "help")):
    print(how_to_use)
    exit(1)

# URL to RATP CSV dataset    
dataset = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"

# If arguments are provided, use path to dataset. If not, URL is used by default.
if (arguments == 2):
    dataset = sys.argv[1]

dataframe = loadData(dataset)
display(dataframe)

dataframe.hist(column='Trafic', bins=26, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
trafic = dataframe['Trafic'].tolist()
stations = dataframe['Station'].tolist()
# x = range(1, len(stations) +1)
# plt.xticks(np.array(x), stations)
# plt.plot(x, trafic)
plt.show()

