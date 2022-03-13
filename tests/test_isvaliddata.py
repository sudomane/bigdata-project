import pytest

url = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=json&timezone=Europe/Berlin&lang=fr"

def test_isvaliddata():
    dataframe = loadData(url)
    assert "Rang" in dataframe