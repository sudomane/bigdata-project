import sys
from dataprocessing import loadData

how_to_use = "Usage: main.py [path to json database]"

arguments = len(sys.argv)

if (arguments == 2 and (sys.argv[1] == 'h' or sys.argv[1] == "help")):
    print(how_to_use)
    exit(1)

# URL to RATP JSON dataset    
dataset = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=json&timezone=Europe/Berlin&lang=fr"

# If arguments are provided, use path to dataset. If not, URL is used by default.
if (arguments == 2):
    dataset = sys.argv[1]

dataframe = loadData(dataset)
