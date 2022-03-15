import sys
import dataprocessing as dp
from IPython.display import display
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

dataframe = dp.loadData(dataset)
display(dataframe)

colors = {
    "1" : "#fecd04",
    "2" : "#006cb8",
    "3" : "#9b983b",
    "3bis" : "#89d3de",
    "4" : "#bd499c",
    "5" : "#f68d49",
    "6" : "#76c595",
    "7" : "#eb96a6",
    "7bis" : "#76c596",
    "8" : "#c3a0ca",
    "9" : "#cdc729",
    "10" : "#deaf39",
    "11" : "#8d6438",
    "12" : "#008c59",
    "13" : "#86cfdb",
    "14" : "#642c8f",
    "A" : "#ff1400",
    "B" : "#3c91dc",
    "C" : "#ffbe00",
    "D" : "#00643c",
    "E" : "#a0006e",
}

dataframe.hist(column='Trafic', bins=26, grid=False, figsize=(12,8), color=colors["1"], zorder=2, rwidth=0.9)
trafic = dataframe['Trafic'].tolist()
stations = dataframe['Station'].tolist()
# x = range(1, len(stations) +1)
# plt.xticks(np.array(x), stations)
# plt.plot(x, trafic)
plt.show()

