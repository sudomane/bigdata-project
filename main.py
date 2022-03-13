import sys
import pandas as pd

how_to_use = "Usage: main.py [path to excel database]"

arguments = len(sys.argv)

if (arguments == 2 and sys.argv[1] == 'h'):
    print(how_to_use)
    exit(1)

# URL to RATP Excel dataset
dataset = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=xls&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true"

# If no arguments are provided, use default dataset.
if (arguments == 2):
    dataset = str(sys.argv[1])
    
# Throw exception if we couldn't load the file, or URL is invalid.
try:
    dataframe = pd.read_excel(dataset)
except Exception as e:
    print(e)
