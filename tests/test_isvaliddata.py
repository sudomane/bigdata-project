import pytest

# Import functions to test
from src.dataprocessing import loadData

url = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
dataframe = loadData(url)
# Simply checking if the column "Rang" is in the dataframe.
# If it is, then the dataframe has been correctly loaded.
# If not, then we need to properly clean the data.
def test_isvaliddata():
    assert "Rang" in dataframe
