import pytest

# Import functions to test
from src.dataprocessing import loadData
from src.dataprocessing import getLineInfo

url = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
dataframe = loadData(url)
dict = getLineInfo(dataframe, "14")

# Checks if dataframe is correctly loaded
def test_isvaliddata_station():
    assert "Station" in dataframe
    
def test_isvaliddata_traffic():
    assert "Trafic" in dataframe
    
def test_isvaliddata_correspondances():
    assert "Correspondances" in dataframe

def test_correctcolumnsize():
    assert dataframe.columns.size == 3

def test_correctindexsize():
    assert dataframe.index.size == 371

def test():
    assert dataframe.iloc[1, 0] == "CHATELET"

# Check if data is correctly loaded for line 14
def test_isvalidinfo():
    assert dict["BIBLIOTHEQUE"] == 10002396

# Check if incorrect data is not in dictionnary
def test_notvalidinfo():
    with pytest.raises(Exception) as e:
        dict["VILLEJUIF"]