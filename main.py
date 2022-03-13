import sys
import pandas as pd

# URL to RATP Excel dataset
dataset = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=xls&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true"

# If no arguments are provided, use default dataset.
if (len(sys.argv) == 2):
    dataset = str(sys.argv[1])
    
# Throw exception if we couldn't load the file, or URL is invalid.
try:
    dataframe = pd.read_excel(dataset)
except Exception as e:
    print(e)
