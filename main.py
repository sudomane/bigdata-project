import sys
import pandas as pd

how_to_use = "Usage: main.py [path to excel database]"

arguments = len(sys.argv)
parameter = sys.argv[1]

if (arguments == 2 and (parameter == 'h' or parameter == "help")):
    print(how_to_use)
    exit(1)

# URL to RATP Excel dataset
dataset = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=xls&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true"

# If arguments are provided, use path to dataset. If not, URL is used by default.
if (arguments == 2):
    dataset = parameter
    
# Throw exception if we couldn't load the file, or URL is invalid.
try:
    dataframe = pd.read_excel(dataset)
except Exception as e:
    print(e)
